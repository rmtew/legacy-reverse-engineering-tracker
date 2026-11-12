# Correct Neuromancer target CPU audit

Align target CPU audit with the documented native 68K Macintosh target.

Date: 2026-11-12 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- neuromancer-iigs-mac68k / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- neuromancer-iigs-mac68k / Runtime profiles (no-evidence-found): No independently verified hardware runtime profile.
- neuromancer-iigs-mac68k / AI (no-evidence-found): AI use was not established from the inspected README and latest commit; absence of disclosure does not prove non-use.

## neuromancer-iigs-mac68k

Project ID: neuromancer-iigs-mac68k · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "neuromancer-iigs-mac68k",
  "target_cpu": [
    "m68k"
  ]
}
```

Expected existing project SHA256: 732557aeb115aac51b6be960000ab934e394c5fb86929c9faae17186b3c3a562

### Identity (reviewed)

Pinned upstream README identifies Neuromancer as the subject.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Classification (reviewed)

Native 68K Macintosh adaptation based on the Apple IIGS game, with monochrome and colour editions; byte-exact reconstruction is not established.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Source CPU (reviewed)

The source is the Apple IIGS game, using 65816.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Target CPU (reviewed)

The README identifies a native 68K Macintosh adaptation; no narrower minimum model is asserted.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Build (reviewed)

The README describes author-reported scope and status. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Runtime profiles (no-evidence-found)

No independently verified hardware runtime profile.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### AI (no-evidence-found)

AI use was not established from the inspected README and latest commit; absence of disclosure does not prove non-use.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

### Relationships (reviewed)

Distinct repository; related projects are not assumed identical.
- https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md

## Pinned evidence manifest

- neuromancer-iigs-mac68k-readme: https://github.com/apple2forever/neuromancer-mac68k/blob/917c5c097eb1c281523abc01af9c77fed1c88fc0/README.md (Git blob 35910c00ede78faa75f990f0919a2d110897ff15)

## Research event notes

Correct the contradictory target CPU audit narrative in the discovery batch.
