# Repository audit for Paper B

- Audit date: 2026-08-13
- Updated: 2026-08-14
- Scope: `mibo-research-pilot/queries` only

## Findings and disposition

- Later repository maintenance had overwritten `v0.1.json` and `v0.1.0.json` with `v0.1.1` content, making their root filenames historically misleading.
- The authentic `v0.1.json` bytes were recovered from commit `868672e407c4ec8183a4e99d5c4b64c04a175b35`; their Git blob SHA is `fa433874368614bc3eef5cf946d493fd9d552564`.
- The authentic `v0.1.0.json` bytes were recovered from the same commit; their Git blob SHA is `710da3b5808fdce693fd40514bd4a8edb1ba08c1`.
- `v0.1.1.json` was restored separately as the five-query MIBO Pilot operational instrument used for the Paper B evidence freeze.
- No historical or operational query wording was reconstructed from memory.
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
- Automated validation: `python scripts/validate_queries.py` passed all checks.

## Changed files

- `README.md`: corrected repository role, terminology, version provenance, and the distinction among the operational instrument, Paper B freeze, and continuing Pilot.
- `v0.1.json`: restored byte-for-byte from historical Git blob `fa433874368614bc3eef5cf946d493fd9d552564`.
- `v0.1.0.json`: restored byte-for-byte from historical Git blob `710da3b5808fdce693fd40514bd4a8edb1ba08c1`.
- `v0.1.1.json`: restored separately as the Paper B operational snapshot; its query content remains unchanged.
- `HASHES.json`: scoped explicitly to `v0.1.1.json` without changing any digest.
- `scripts/validate_queries.py`: added repository validation for JSON, exact query texts, IDs, counts, and hashes.
- `.github/workflows/validate.yml`: added validation on pushes and pull requests.
- `AUDIT.md`: added this scoped audit and validation record.

`LICENSE` was intentionally left unchanged. No repository under `mibo-research` was modified.

## Unresolved issues

None.
