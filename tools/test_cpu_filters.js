"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const { test } = require("node:test");

const root = path.resolve(__dirname, "..");
const source = fs.readFileSync(path.join(root, "web/tracker.js"), "utf8");
const catalogue = JSON.parse(fs.readFileSync(path.join(root, "data/projects.json"), "utf8"));
const node = () => ({
  value: "",
  dataset: {},
  classList: { contains: () => false, toggle: () => {} },
  addEventListener: () => {},
  setAttribute: () => {},
  querySelectorAll: () => [],
  close: () => {}
});
const elements = new Map();
const context = vm.createContext({
  document: {
    documentElement: { dataset: {} },
    getElementById: id => {
      if (!elements.has(id)) elements.set(id, node());
      return elements.get(id);
    },
    querySelector: () => node(),
    querySelectorAll: () => []
  },
  window: { matchMedia: () => ({ matches: false, addEventListener: () => {} }) },
  fetch: () => new Promise(() => {}),
  localStorage: { setItem: () => {} },
  console,
  Date,
  Set,
  Map,
  Promise
});
vm.runInContext(source, context, { filename: "web/tracker.js" });
const family = value => vm.runInContext(`cpuFamily(${JSON.stringify(value)})`, context);
const choose = value => vm.runInContext(`projectFilterState.cpu = new Set([${JSON.stringify(value)}])`, context);
const matches = record => {
  context.testRecord = record;
  return vm.runInContext("matches(testRecord)", context);
};
const families = record => {
  context.testRecord = record;
  return [...vm.runInContext("cpuFamilyValues(testRecord)", context)];
};

test("CPU family selection matches source, target and verified runtime CPU", () => {
  choose("68000 family");
  assert.equal(matches({ source_cpu: ["m68000"] }), true);
  assert.equal(matches({ source_cpu: [], target_cpu: ["m68020"] }), true);
  assert.equal(matches({ source_cpu: [], target_cpu: [], runtime_profiles: [{platform:"Amiga", min_cpu:"68030"}] }), true);
  assert.equal(matches({ source_cpu: ["Z80"] }), false);
  choose("6502 family");
  assert.equal(matches({ source_cpu: ["6502"] }), true);
  assert.equal(matches({ source_cpu: ["65C12"] }), true);
});

test("common CPU variants share their discovery family", () => {
  for (const value of ["6502", "6507", "65C02", "65C12", "65C102", "65816", "HuC6280"]) {
    assert.equal(family(value), "6502 family", value);
  }
  for (const value of ["m68000", "m68020", "68040", "m68k"]) {
    assert.equal(family(value), "68000 family", value);
  }
  for (const value of ["8086", "80286", "i386", "x86-64"]) {
    assert.equal(family(value), "x86", value);
  }
});

test("facet results equal family membership across the live catalogue", () => {
  for (const value of ["68000 family", "6502 family"]) {
    choose(value);
    const expected = catalogue.filter(record => families(record).includes(value)).length;
    const actual = catalogue.filter(matches).length;
    assert.ok(expected > 100, `${value} should have substantial catalogue coverage`);
    assert.equal(actual, expected, value);
  }
});

test("platform and CPU must belong to the same side or verified runtime profile", () => {
  vm.runInContext('projectFilterState.platform = new Set(["Amiga"]); projectFilterState.cpu = new Set(["68000 family"]);', context);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["Z80"]}), false);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["68020"]}), true);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],runtime_profiles:[{platform:"Amiga",min_cpu:"68000"}]}), true);
  vm.runInContext('projectFilterState.side="source";', context);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["68020"]}), false);
  vm.runInContext('projectFilterState.platform = new Set(["Atari ST"]);', context);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["Z80"]}), true);
  vm.runInContext('projectFilterState.side="either"; projectFilterState.platform.clear(); projectFilterState.cpu.clear();', context);
});

test("port route keeps both sides distinct and same-family needs evidence on both", () => {
  vm.runInContext('projectFilterState.directionMode="route"; projectFilterState.sourcePlatform=new Set(["Atari ST"]); projectFilterState.targetPlatform=new Set(["Amiga"]); projectFilterState.sameFamily=true;', context);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["68020"]}), true);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["Z80"]}), false);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:[]}), false);
  assert.equal(matches({source_platforms:["Amiga"],source_cpu:["68000"],target_platforms:["Atari ST"],target_cpu:["68000"]}), false);
  vm.runInContext('projectFilterState.sameFamily=false; projectFilterState.sourceCpu=new Set(["Z80"]);', context);
  assert.equal(matches({source_platforms:["Atari ST"],source_cpu:["68000"],target_platforms:["Amiga"],target_cpu:["68020"]}), false);
  vm.runInContext('projectFilterState.directionMode="quick"; projectFilterState.sourcePlatform.clear(); projectFilterState.targetPlatform.clear(); projectFilterState.sourceCpu.clear();', context);
});

test("execution filter includes mixed projects while leaving unclassified records visible by default", () => {
  const battle = catalogue.find(record => record.id === "battle-squadron-amiga-recomp-crownpark");
  const moonstone = catalogue.find(record => record.id === "moonstone-amiga-windows-undine1");
  const unknown = catalogue.find(record => !record.execution_paths);
  assert.ok(battle && moonstone && unknown);
  assert.equal(matches(unknown), true);
  vm.runInContext('projectFilterState.execution = new Set(["game-specific-emulation"]);', context);
  assert.equal(matches(battle), true);
  assert.equal(matches(moonstone), true);
  assert.equal(matches(unknown), false);
  vm.runInContext('projectFilterState.execution = new Set(["native-translation"]);', context);
  assert.equal(matches(battle), true);
  assert.equal(matches(moonstone), false);
  context.testRecord = battle;
  const badges = vm.runInContext('executionBadges(testRecord)', context);
  assert.match(badges, /Game-specific emulation/);
  assert.match(badges, /Native translation: partial/);
  vm.runInContext('projectFilterState.execution.clear();', context);
});
