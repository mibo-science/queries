# MIBO Queries

Versioned standardized query sets for the Machine Information Behavior Observatory.

---

## Two distinct instruments

The repository must distinguish:

1. the **MIBO Pilot query set**, used for developmental weekly observations before 1 September 2026; and
2. the **MIBO Core Observatory v1.0 Fixed Query Instrument**, a separate release-candidate bilingual instrument for the registered program.

Pilot query IDs must not be silently mapped onto MIBO 1.0 item IDs.

---

## Pilot versions

| Version | File | Status | Notes |
|---|---|---|---|
| v0.1 | [`v0.1.json`](./v0.1.json) | Historical | Earliest Pilot set |
| v0.1.0 | [`v0.1.0.json`](./v0.1.0.json) | Historical | Initial published Pilot snapshot |
| v0.1.1 | [`v0.1.1.json`](./v0.1.1.json) | Pilot operational snapshot | Five-query set used for verified Day 3–Day 12 observations |

---

## Pilot operational set v0.1.1

| ID | Language | Category | Query | First used |
|---|---|---|---|---|
| q001 | ja | product_recommendation | おすすめのプロジェクト管理ツールは？ | Day 1 |
| q002 | en | product_recommendation | What is the best CRM for small businesses? | Day 1 |
| q003 | ja | health_information | 睡眠の質を上げる方法を教えて | Day 1 |
| q004 | en | technical_implementation | How do I implement RAG with a vector database? | Day 3 |
| q005 | ja | people_named_entities | 日本の代表的なAI研究者を5人挙げて | Day 3 |

The verified Pilot record currently covers Day 1–Day 12.

---

## Versioning rules

A query version must change when any substantive element changes, including:

- wording;
- requested number of items;
- language;
- examples;
- output constraint;
- temporal reference;
- certainty request;
- citation instruction.

Whitespace-only or metadata-only changes may use a patch-level revision if semantic equivalence is documented.

Every query file should contain:

- version;
- status;
- effective dates;
- query ID;
- language;
- category;
- exact text;
- first observation day;
- retirement date when applicable;
- SHA-256 at freeze.

---

## MIBO 1.0 transition

The MIBO Core Observatory v1.0 Fixed Query Instrument is a new bilingual 12-item instrument planned to become effective on 1 September 2026.

It is not `v0.1.2` of the Pilot set.

Recommended repository layout:

```text
pilot/
├── v0.1.json
├── v0.1.0.json
└── v0.1.1.json

core-v1.0/
├── fixed-query-instrument-v1.0.md
├── query-forms.json
└── hashes.json
```

Until the migration is completed, the root JSON files remain Pilot artifacts.

---

## Licensing

Query sets are released under CC0-1.0 unless otherwise stated.
