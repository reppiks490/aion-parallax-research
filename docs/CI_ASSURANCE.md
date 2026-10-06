# CI assurance contract

This repository uses `.github/workflows/parallax-tests.yml` as its continuous
assurance layer.

## Change-time gates

Pushes to `main`, pull requests, merge-queue checks, and manual dispatches run:

- Python 3.11, 3.12, and 3.13 compilation and the full unit suite.
- JSON contract parsing.
- Cockpit inline JavaScript syntax validation with Node.
- An isolated synthetic demo/replay/verification path.
- Wheel/sdist build, installed CLI smoke test, and `pip check`.
- A final aggregate gate.

The workflow deliberately does not authenticate real market data, place orders,
or transform synthetic evidence into a performance claim.

## Scheduled drift gate

The daily schedule runs one Python 3.12 drift job rather than the full matrix. It
rechecks compilation, tests, contracts, cockpit syntax, dependency consistency,
and the isolated synthetic replay path.

## Machine-readable evidence

Every aggregate gate writes `assurance/assurance-summary.json` and uploads it
as a 30-day workflow artifact. The document records repository, workflow, run,
event, commit, ref, authority, execution permission, gate results, and final
result. It is designed for durable owner automation or UI ingestion without
granting execution authority.

AION evidence declares `authority=read_only_research` and
`execution_allowed=false`.

## Dependency maintenance automation

Dependabot checks GitHub Actions and Python packaging metadata every Monday in
`America/Chicago`. Minor and patch updates are grouped to reduce pull-request
noise; major updates remain isolated for explicit review. Dependency changes that
touch `pyproject.toml` or workflow files are still subject to the repository's
normal assurance gates before merge.

