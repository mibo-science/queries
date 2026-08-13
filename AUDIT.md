# Repository audit for Paper B

- Audit date: 2026-08-13
- Scope: `mibo-research-pilot/queries` only

## Findings and disposition

- `v0.1.1.json` was referenced by `README.md` but missing. It was restored from the authoritative `e98e3ae407dcb051f20bb8a4f93e9e97f679b0da` Git blob already tracked as both `v0.1.json` and `v0.1.0.json`; it was not reconstructed from memory.
- The three versioned JSON paths now resolve to the same committed content. `v0.1.json` and `v0.1.0.json` are intentionally preserved as historically meaningful paths, while their earlier states remain in Git history.
- Git history contains a provisional 2026-05-05 state of `v0.1.json` that listed q004–q005 before operational use. The 2026-05-07 revision removed them. That history is preserved, but the verified operational chronology is q001–q003 from Day 1 and q004–q005 from Day 3.
- `README.md` previously described Day 13 as a current Pilot boundary and included forward-looking Core instrument design. It now separates the Pilot operational instrument, the Paper B evidence freeze, and the continuing pre-2026-09-01 Pilot phase; out-of-scope Core design details were removed.
- The current MIBO expansion is standardized to “MIBO — Machine Information Behavioral Observatory.” Historical wording remains untouched in Git history.
- The missing local link to `v0.1.1.json` is fixed. All other local links resolve, and the linked `mibo-research-pilot/core` and `mibo-research-pilot/reports` repositories exist.
- `LICENSE` is the CC0 1.0 Universal legal code. No disposable generated or temporary files were found, so no files were deleted.

## Validation

- JSON parsing: passed for `HASHES.json`, `v0.1.json`, `v0.1.0.json`, and `v0.1.1.json`.
- Per-query SHA-256: passed for q001–q005 using each exact UTF-8 `text` value.
- Instrument SHA-256: passed using `id<TAB>language<TAB>category<TAB>text<LF>` in query order.
- Verified instrument hash: `8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35`.
- Exact query wording: unchanged.

## Changed files

- `README.md`: corrected repository role, terminology, version provenance, and the distinction among the operational instrument, Paper B freeze, and continuing Pilot.
- `v0.1.1.json`: added from an authoritative existing repository blob.
- `AUDIT.md`: added this scoped audit and validation record.

`HASHES.json`, `v0.1.json`, `v0.1.0.json`, and `LICENSE` were intentionally left unchanged. No repository under `mibo-research` was modified.

## Unresolved issues

None.
