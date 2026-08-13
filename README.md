# MIBO Queries

**Repository:** `mibo-research-pilot/queries`  
**Official GitHub organization:** `mibo-research-pilot`  
**Collection surface:** API-based from Day 1 — 2026-05-05  
**Paper B evidence freeze:** Day 13 — 2026-07-28 — 244 included observations<br>
**Pilot phase:** continued after the Paper B freeze and before 2026-09-01

Versioned standardized query instruments for **MIBO — Machine Information Behavioral Observatory**.

---

## Repository role

This repository is the historical, citation-ready record of the query instrument used in the MIBO Pilot.

Its functions are to:

- freeze exact query wording;
- record query-set versions;
- distinguish semantic query changes from metadata updates;
- record first-use and retirement boundaries;
- preserve language and category labels;
- provide cryptographic hashes for integrity checking;
- prevent silent remapping of Pilot query IDs to item IDs from a later project phase.

Related repositories:

- [`mibo-research-pilot/core`](https://github.com/mibo-research-pilot/core) — concepts, methodology, hierarchy, and claim registry;
- [`mibo-research-pilot/reports`](https://github.com/mibo-research-pilot/reports) — API observation records and longitudinal analyses.

---

## Scope and evidence boundary

Three boundaries must be kept separate:

| Boundary | Meaning |
|---|---|
| MIBO Pilot operational instrument `v0.1.1` | The five-query operational query set from Day 3 onward |
| Paper B evidence freeze | Day 13, 2026-07-28, with 244 included observations |
| Continuing Pilot phase | Pilot observations after Day 13 and before 2026-09-01; these are outside the Paper B evidence freeze, not outside the Pilot |

Work beginning on or after 2026-09-01 belongs to the separate MIBO Core project phase and is outside this repository's scope. Pilot query IDs must not be silently mapped to later MIBO Core item IDs.

---

## Pilot versions

| Version | File | Status | Notes |
|---|---|---|---|
| v0.1 | [`v0.1.json`](./v0.1.json) | Historical legacy path | Early three-query snapshot containing q001–q003. Its original internal schema and version wording are preserved exactly, although the filename and internal version convention are not perfectly aligned. |
| v0.1.0 | [`v0.1.0.json`](./v0.1.0.json) | Initial published Pilot snapshot | Effective from 2026-05-05 and containing q001–q003. |
| v0.1.1 | [`v0.1.1.json`](./v0.1.1.json) | Pilot operational instrument | Five-query set used from Day 3 onward. Paper B evidence freeze: Day 13 / 2026-07-28 / 244 included observations. |

The historical artifacts were recovered byte-for-byte from Git history after later maintenance had overwritten their root copies. See [`AUDIT.md`](./AUDIT.md) for provenance and verification.

---

## Pilot operational set v0.1.1

| ID | Language | Category | Exact query text | First used |
|---|---|---|---|---|
| q001 | ja | `product_recommendation` | おすすめのプロジェクト管理ツールは？ | Day 1 — 2026-05-05 |
| q002 | en | `product_recommendation` | What is the best CRM for small businesses? | Day 1 — 2026-05-05 |
| q003 | ja | `health_information` | 睡眠の質を上げる方法を教えて | Day 1 — 2026-05-05 |
| q004 | en | `technical_implementation` | How do I implement RAG with a vector database? | Day 3 — 2026-05-19 |
| q005 | ja | `people_named_entities` | 日本の代表的なAI研究者を5人挙げて | Day 3 — 2026-05-19 |

### Observation schedule

| Sessions | Active query IDs | Queries per system |
|---|---|---:|
| Day 1–Day 2 | q001–q003 | 3 |
| Day 3 onward during the Pilot | q001–q005 | 5 |

Collection was API-based continuously from Day 1.

Day 13 is the Paper B evidence freeze, not the end of the MIBO Pilot.

The API transport does not change the exact query text.

---

## Exact-text rule

The `text` field is the canonical query stimulus.

The following must not be added silently during execution:

- system-specific examples;
- citation requests;
- requests for prices or dates;
- requests for tables;
- requests for a particular number of products unless already present;
- temporal qualifiers;
- geographic qualifiers;
- certainty qualifiers;
- safety disclaimers;
- output-language instructions;
- hidden paraphrases.

Provider-required system or developer messages must be recorded separately from the fixed user query.

The query instrument is not defined by the response format produced by a provider.

---

## Versioning rules

A query-set version must change when a substantive stimulus element changes.

Examples include:

- query wording;
- language;
- requested number of items;
- examples;
- output constraints;
- temporal reference;
- geographic reference;
- certainty request;
- citation instruction;
- role instruction;
- comparison frame.

### Recommended version interpretation

| Change type | Version action |
|---|---|
| Query meaning or stimulus changed | Minor or major version |
| Query added or retired | Minor or major version |
| Category label clarified without changing the stimulus | Patch version or metadata revision |
| Verified-through day/date updated | No semantic version change |
| Typographic or whitespace correction with documented semantic equivalence | Patch version |
| File-format or schema metadata updated | Schema-version or metadata update |

The Day 13 Paper B evidence freeze changes only the cited evidence boundary. It does not end the Pilot or change the exact five query texts, so the operational instrument remains `v0.1.1`.

---

## Integrity and hashing

[`HASHES.json`](./HASHES.json) applies only to the five-query `v0.1.1.json` instrument. It does not describe either historical three-query artifact.

Each query in `v0.1.1.json` contains:

- `exact_text_sha256`;
- `exact_text_frozen`;
- first-use metadata;
- retirement status.

The file also contains an `instrument_content_sha256`.

The instrument hash is calculated from the UTF-8 concatenation of the five records in query order:

```text
id<TAB>language<TAB>category<TAB>text<LF>
```

Instrument content SHA-256:

```text
8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35
```

Hashing verifies exact text and coding labels. It does not prove that a provider executed the query under identical service conditions.

---

## Required observation linkage

Every observation record should identify:

- query-set version;
- query ID;
- exact query-text hash;
- API request timestamp;
- API response timestamp;
- provider and service lineage;
- exact model identifier or recorded label;
- request parameters;
- locale and language;
- tool or retrieval state;
- raw response or auditable evidence;
- correction status.

The query-set file and observation metadata should be sufficient to determine which exact stimulus was used.

---

## Query corrections

A correction to an observation response does not normally change the query-set version.

Examples:

- replacing a duplicated response with the correct response;
- correcting an example date inside a stored response;
- correcting coding or source classification;
- updating verified cumulative counts.

A query-set version changes only when the stimulus or its operational meaning changes.

---

## Naming rules

Use:

- MIBO — Machine Information Behavioral Observatory;
- MIBO Pilot;
- `mibo-research-pilot/queries`.

Avoid:

- silently treating Pilot `v0.1.1` as an instrument from a later project phase;
- describing Day 13 / 244 observations as the end of the entire Pilot;
- silently changing exact query text;
- using any repository organization other than `mibo-research-pilot`.

---

## Licensing

Query sets are released under CC0-1.0 unless otherwise stated.

Raw responses generated from these queries remain subject to applicable provider terms.
