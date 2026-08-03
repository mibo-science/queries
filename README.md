# MIBO Queries

**Repository:** `mibo-research-pilot/queries`  
**Official GitHub organization:** `mibo-research-pilot`  
**Collection surface:** API-based from Day 1 — 2026-05-05  
**Current verified Pilot boundary:** Day 13 — 2026-07-28  
**Verified cumulative observations:** 244

Versioned standardized query instruments for the **Machine Information Behavior Observatory — MIBO**.

---

## Repository role

This repository preserves the exact query instruments used in MIBO observations.

Its functions are to:

- freeze exact query wording;
- record query-set versions;
- distinguish semantic query changes from metadata updates;
- record first-use and retirement boundaries;
- preserve language and category labels;
- provide cryptographic hashes for integrity checking;
- prevent silent remapping between the MIBO Pilot and MIBO Core v1.0 instruments.

Related repositories:

- [`mibo-research-pilot/core`](https://github.com/mibo-research-pilot/core) — concepts, methodology, hierarchy, and claim registry;
- [`mibo-research-pilot/reports`](https://github.com/mibo-research-pilot/reports) — API observation records and longitudinal analyses.

---

## Two distinct instruments

The repository distinguishes two separate instruments.

### MIBO Pilot query set

The MIBO Pilot query set is the developmental instrument used before 1 September 2026.

The current operational snapshot is `v0.1.1`.

### MIBO Core v1.0 Fixed Query Instrument

MIBO Core v1.0 is a separate registered instrument planned to become effective on 1 September 2026.

It is not a patch release of the Pilot set.

```text
Pilot v0.1.1 ≠ MIBO Core v1.0
```

Pilot query IDs must not be silently mapped onto MIBO Core v1.0 item IDs.

Any crosswalk must be explicit, versioned, and analytically justified.

---

## Pilot versions

| Version | File | Status | Notes |
|---|---|---|---|
| v0.1 | `v0.1.json` | Historical | Earliest three-query Pilot set |
| v0.1.0 | `v0.1.0.json` | Historical | Initial published Pilot snapshot |
| v0.1.1 | [`v0.1.1.json`](./v0.1.1.json) | Operational Pilot snapshot | Five-query set used from Day 3 and verified through Day 13 |

The historical files remain historical artifacts. Their exact content must not be reconstructed from memory if the original files are unavailable.

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
| Day 3–Day 13 | q001–q005 | 5 |

All observations have been conducted through APIs from Day 1.

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

The Day 13 update changes only the verified evidence boundary and integrity metadata. The exact five query texts remain unchanged, so the instrument remains `v0.1.1`.

---

## Integrity and hashing

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

## MIBO Core v1.0 transition

Recommended repository layout:

```text
pilot/
├── v0.1.json
├── v0.1.0.json
└── v0.1.1.json

core-v1.0/
├── fixed-query-instrument-v1.0.md
├── query-forms.json
├── hashes.json
└── crosswalk-from-pilot.json
```

Until migration is completed, the root `v0.1.1.json` remains the authoritative operational Pilot snapshot.

The crosswalk file must distinguish:

- exact reuse;
- translation;
- semantic adaptation;
- category replacement;
- retirement;
- no correspondence.

Pilot results must not be presented as if they were collected with the MIBO Core v1.0 instrument.

---

## Naming rules

Use:

- MIBO;
- MIBO Pilot;
- MIBO Core v1.0;
- Fixed Query Instrument;
- `mibo-research-pilot/queries`.

Avoid:

- adding a redundant “Observatory” suffix to MIBO Core;
- silently treating Pilot v0.1.1 as MIBO Core v1.0;
- silently changing exact query text;
- using any repository organization other than `mibo-research-pilot`.

---

## Licensing

Query sets are released under CC0-1.0 unless otherwise stated.

Raw responses generated from these queries remain subject to applicable provider terms.
