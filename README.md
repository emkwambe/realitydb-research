# RealityDB AI Assurance Research

Research repository for investigating how regulated and enterprise companies build evaluation, testing, monitoring, and assurance infrastructure for production AI agents.

## Research objective

Determine whether RealityDB should extend from synthetic data generation into production-realistic AI evaluation scenarios, benchmark datasets, testing environments, and assurance infrastructure.

## Core question

How are regulated and enterprise companies building evaluation, testing, and assurance infrastructure for production AI agents?

## Industries

- Healthcare
- Insurance
- Financial services
- Customer support platforms
- Enterprise SaaS
- Legal technology

## Repository structure

- `docs/` — research scope, methodology, taxonomy, decision logs
- `sources/` — source registry and citation tracking
- `data/raw/` — unprocessed job postings and source captures
- `data/processed/` — normalized research datasets
- `analysis/` — synthesis, scoring, and market analysis
- `notebooks/` — exploratory analysis notebooks
- `reports/` — draft and final reports
- `templates/` — structured extraction templates
- `scripts/` — collection, cleaning, and analysis utilities

## Recommended workflow

1. Register every source in `sources/source_registry.csv`.
2. Capture job postings using `templates/job_posting_extraction.yaml`.
3. Capture company and technical evidence using `templates/company_evidence_extraction.yaml`.
4. Normalize records into `data/processed/`.
5. Analyze recurring capabilities using `analysis/capability_taxonomy.md`.
6. Score candidate niches using `analysis/niche_scoring.csv`.
7. Draft conclusions in `reports/research_report_outline.md`.

## Research discipline

- Prefer primary sources.
- Separate facts from inference.
- Record publication and access dates.
- Do not treat job-posting volume alone as proof of demand.
- Capture contradictory evidence.
- Identify the narrowest product wedge that strengthens RealityDB.
