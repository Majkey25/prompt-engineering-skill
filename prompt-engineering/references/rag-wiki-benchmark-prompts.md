# RAG, Wiki, VDB, Raw Data, Hot Cache, and Benchmark Prompts

Use this file when the user asks for prompts, agent tasks, or internal task briefs involving RAG, search, vector databases, wiki systems, document QA, cached answers, raw data pipelines, retrieval quality, indexing, chunking, embeddings, citations, benchmark datasets, or evaluation harnesses.

## Core doctrine

RAG quality is not "the model answers nicely." RAG quality means:

- right sources are ingested
- right chunks are retrieved
- metadata is correct
- stale data is not served
- citations point to real source material
- answer only claims what sources support
- failure modes are explicit
- benchmarks include hard negative cases

Treat the model as the last stage, not the whole system.

## Universal RAG prompt structure

```text
# Goal
Build / debug / evaluate [RAG or wiki task].

# Communication
Be concise. Keep validation and evidence. Use compact checklists/tables when useful.

# Context
- corpus:
- source formats:
- index/vector DB:
- embed model:
- retriever:
- answer model:
- known failures:

# Non negotiable
- Do not trust generated answers without source evidence.
- Inspect raw source -> parsed text -> chunks -> metadata -> embeddings -> retrieval -> final answer.
- Do not hide missing sources.
- Do not fake citations.
- Do not tune only on easy questions.
- Report exact commands, sample queries, retrieved chunks, and failure cases.

# Process
1. Inventory data sources.
2. Check parsing/extraction quality.
3. Check chunking and metadata.
4. Check indexing and stale/deleted docs.
5. Run retrieval-only tests before answer tests.
6. Run answer tests with citations.
7. Add hard negative questions.
8. Review failures and fix root cause.

# Verification
- run ingestion on sample docs
- query known-answer questions
- query impossible questions
- check retrieved chunks
- check citation validity
- check stale cache behavior
- check deleted/updated document behavior

# Output
- what changed
- files/config changed
- commands run
- benchmark table
- failures found/fixed
- remaining risks
```

## Raw data checks

Require the agent to inspect each layer:

1. source file exists
2. parser reads correct text
3. tables/images are handled or explicitly unsupported
4. chunk text is not empty/duplicated/broken
5. chunk metadata has source id, path/name, page/section, timestamp/version when available
6. vector DB has only current chunks
7. deleted files remove stale chunks
8. updated files replace old chunks
9. retrieval returns expected source for known query
10. impossible query returns "not found" or constrained answer, not hallucination

## Hot cache rules

For hot cache / cached answer / precomputed retrieval prompts:

- Define cache key inputs exactly.
- Include corpus version or document checksum in cache key when correctness matters.
- Invalidate cache on source update, deletion, permission change, or parser change.
- Never serve cached answer across users if permissions differ.
- Log whether answer came from cache or fresh retrieval.
- Verify stale-cache failure with at least one update/delete scenario.

## Benchmark design

A serious RAG benchmark needs:

- 10+ representative questions minimum for small systems
- known-answer questions
- multi-hop questions
- citation-required questions
- hard negatives where corpus lacks the answer
- stale/update/delete cases
- ambiguous wording cases
- permission or visibility cases if applicable
- scoring rubric: retrieval hit, answer correctness, citation correctness, refusal correctness, latency/cost if relevant

## Benchmark output table

```text
| Case | Expected | Retrieved source | Answer OK | Citation OK | Notes |
|---|---|---|---|---|---|
| Q1 | ... | ... | yes/no | yes/no | ... |
```

## Anti-patterns

Bad:

```text
Improve the RAG.
```

Better:

```text
Inspect ingestion -> parsing -> chunking -> metadata -> vector DB -> retrieval -> answer generation. Build 10 benchmark questions including impossible and stale-data cases. Fix root causes for retrieval or citation failures. Report exact evidence.
```

Bad:

```text
Make the wiki smarter.
```

Better:

```text
Define target wiki workflows, inspect current search/retrieval path, test known pages and missing pages, verify citations, check stale cache behavior, and produce a benchmark table before claiming improvement.
```
