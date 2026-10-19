"""Shared request, wall-time and per-record limits for network collection."""

import time


class BudgetStop(Exception):
    scope = "global"


class LaneStop(BudgetStop):
    scope = "lane"


class APIStop(BudgetStop):
    scope = "api"


class FetchFailure(Exception):
    def __init__(self, message, *, rate_limited=False):
        super().__init__(message)
        self.rate_limited = rate_limited


class RecordStop(FetchFailure):
    pass


class Budget:
    def __init__(self, seconds=600, requests=300, *, api_requests=80, clock=time.monotonic):
        if seconds <= 0 or requests < 0:
            raise ValueError("Collection budgets must be positive (requests may be zero)")
        self.clock, self.start = clock, clock()
        self.deadline, self.limit = self.start + seconds, requests
        self.requests, self.statuses, self.http_seconds, self.cache_hits = 0, {}, 0.0, 0
        self.lane_name, self.lane_limit, self.lane_deadline, self.lanes = None, None, None, {}
        self.api_limit, self.api_requests, self.lane_api_limit = api_requests, 0, None
        self.record_deadline = None

    def check(self, reserve=0):
        if self.clock() >= self.deadline:
            raise BudgetStop("wall-time budget")
        if self.requests + reserve > self.limit:
            raise BudgetStop("request budget")
        if self.lane_deadline is not None and self.clock() >= self.lane_deadline:
            raise LaneStop("lane wall-time budget")
        if self.lane_limit is not None and self.requests + reserve > self.lane_limit:
            raise LaneStop("lane request budget")
        if self.record_deadline is not None and self.clock() >= self.record_deadline:
            raise RecordStop("record wall-time budget")

    def begin_record(self):
        self.record_deadline = self.clock() + 30

    def end_record(self):
        self.record_deadline = None

    def begin_lane(self, name, requests, deadline, api_requests=None):
        self.lane_name = name
        self.lane_limit = self.requests + max(0, requests)
        self.lane_deadline = min(self.deadline, deadline)
        self.lane_api_limit = (
            self.api_limit if api_requests is None else self.api_requests + max(0, api_requests)
        )
        self.lanes.setdefault(name, 0)

    def end_lane(self):
        self.lane_name = self.lane_limit = self.lane_deadline = self.lane_api_limit = None

    def before_request(self, *, api=False):
        self.check(1)
        if api and self.api_requests >= self.api_limit:
            raise APIStop("API request budget")
        if api and self.lane_api_limit is not None and self.api_requests >= self.lane_api_limit:
            raise LaneStop("lane API request budget")
        self.requests += 1
        self.api_requests += int(api)
        if self.lane_name:
            self.lanes[self.lane_name] += 1
        deadline = min(
            self.deadline, self.lane_deadline or self.deadline, self.record_deadline or self.deadline
        )
        return min(10.0, max(0.05, deadline - self.clock()))

    def summary(self):
        return {
            "requests": self.requests,
            "request_limit": self.limit,
            "api_requests": self.api_requests,
            "api_limit": self.api_limit,
            "statuses": self.statuses,
            "http_seconds": round(self.http_seconds, 3),
            "elapsed_seconds": round(self.clock() - self.start, 3),
            "cache_hits": self.cache_hits,
            "lanes": dict(self.lanes),
        }
