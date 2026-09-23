# Current state — 2026-09-23

## Goal

Build AION as the shared decision-time market memory and an explorable time-machine cockpit for the Icarus stack. The owner explicitly requested the more compelling, interactive version and authorized implementation.

## New owner request — proposed next layer

The owner requested one exceptionally interesting hybrid build using primarily the expected ~800 CSVs and asked for GitHub access so every agent can share the work. `docs/PARALLAX-PROPOSAL.md` is the proposed AION extension, **not an implementation**. On 2026-09-23, GitHub browser access as `reppiks490` revealed a second public archive: `csv-data-multi-chart-type` at `a482e7d1801fa7fa5aec093960097c0051c0403c` has 33 usable CSV members in one ZIP, 29 byte-distinct from the earlier nine ZIPs. Together with `multi-level-csv` at `ce82124352762c14eb33836a5c894bc3a2a71dfe`, the accessible checkpoint has **659 usable archive entries across ten ZIPs, 542 byte-distinct contents and roughly 13,787,630 data rows**. Reconcile the expected ~800 before claiming complete coverage. Browser sign-in was confirmed; remote write has not yet been verified.

## Completed in this local repository

- Source and observation contracts, source capability/evidence-tier firewall.
- Append-only hash-linked SQLite event ledger, revisions, as-of queries, gap recovery and tamper detection.
- Immutable evidence-bound forecasts and later outcome settlement.
- Deterministic price/flow/book/macro replay, causal pivot confirmation, separated chart representations and descriptive cross-asset terrain.
- Labeled volatility, depth, macro and source-loss scenarios.
- Loopback, read-only time-machine cockpit, evidence detail, four-system preview packets and a fully synthetic demo.
- JSON Schemas for source, observation and prediction exchange fields in `contracts/`.
- Standard-library `unittest` suite covering timing, identity, immutability, gap recovery, source labels, scenario labels and HTTP outcome hiding.

## Verification

On 2026-09-23: `python -m unittest discover -s tests -v` passed 11/11; `python -m compileall -q aion tests` passed; inline cockpit JS extracted to `/tmp/aion-cockpit-check.js` and `node --check` passed; all three contract files parsed as JSON. CLI `demo` created 21 synthetic observations; `verify` reported 21 verified events with head `7c2318e38cba1ce4648860aeaa613d6ca461a5cee98982d9ff90387258967064`. A `frame` plus `export_views` check confirmed all four packets retain `synthetic: true` and `execution_authorized: false`. No real-data acceptance, browser screenshot or live integration has been run.

## Ownership and known constraints

- The accessible public Icarus checkout was `main` at `007e701`; its isolated ML branch was `codex/ml-d9d4db8` at `e89acba`. This repository does not merge either branch.
- DAEDALUS, ATHENA and ARGUS were reviewed through saved 2026-09-23 handoff packages, not the current private Claude Code working trees. Their interface shapes require confirmation against live commits before linking adapters.
- The two current CSV clones have ten ZIP archives and 659 usable CSV members; this is not verified as the owner's expected 800+ authoritative corpus. The new archive includes ETHUSD, which `Icarus/ASTRA_DO_NOT.md` excludes from model and engine work. AION's demo uses none of those files.
- `SourceSpec` declarations require human/provider review. A digest and a text provenance reference alone do not authenticate licensed market data.
- `Observation.ingested_ns` is supplied by the caller; a production adapter must use a trusted receipt clock and preserve provider proof.
- Book replay currently supports reviewed snapshots and absolute `set/delete` depth updates. Venue-specific incremental semantics and trades/corrections need their own adapters.
- Depth streams require contiguous source sequences. Their gaps and recovery transitions are stored with availability times, so old frames keep their prior quality state. Corrections on sequenced streams are rejected until a provider-specific semantics review.
- Scenario outputs are deterministic stress views, not causal proof or alternative executable fills.
- Browser access to the existing public and private GitHub repositories is confirmed, but a git CLI write credential and remote publication of AION have not been verified. The local source remains unpublished until a verified remote commit; the handoff ZIP is persisted separately.

## Next owner-aligned work

1. Reconcile current Claude Code work and live commits in all four sibling repos. Do not silently overwrite their contracts.
2. Review one real source manifest and implement its provider-specific availability, correction and sequence adapter with tests. Keep licensed raw data outside git.
3. Validate a decision-time replay against a recorded Icarus paper session; compare frame hashes, bar completion and settlement timing.
4. Implement versioned consumer adapters only after owners accept contract mappings; keep them read-only.
5. Record evidence and tests here, then submit separate reviewed changes to each sibling repo.
