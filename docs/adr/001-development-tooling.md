# ADR-001: Development Tooling

**Status**: Accepted
**Date**: 2026-01-17
**Decision Makers**: @hasansezertasan

## Context

As part of modernizing micoo for Python 3.14+, we audited all development tools to evaluate:

1. Overlap and redundancy
2. Value provided vs. maintenance burden
3. Appropriateness for a CLI tool distributed via pipx/uvx/Homebrew

## Decision

### Python Version: 3.14+ Only

For a CLI tool where the distribution method (pipx, uvx, Homebrew) controls the Python version, supporting only the latest stable Python simplifies development without limiting users.

### Type Checking: Keep All Four Tools

| Tool        | Purpose             | Why Keep                                     |
| ----------- | ------------------- | -------------------------------------------- |
| **mypy**    | Static type checker | De-facto standard, best library stub support |
| **pyright** | Static type checker | Stricter analysis, VS Code integration       |
| **ty**      | Static type checker | Rust-based speed, Astral ecosystem alignment |
| **pyrefly** | Static type checker | Different analysis algorithms (Meta)         |

**Rationale**: Each tool catches different edge cases. For a CLI tool that must be reliable, defense-in-depth outweighs the CI time cost.

### Linting & Formatting

| Tool                   | Purpose                | Overlap              | Decision                  |
| ---------------------- | ---------------------- | -------------------- | ------------------------- |
| **ruff**               | Lint + format          | Primary tool         | Keep                      |
| **vulture**            | Dead code              | Partial ruff overlap | Keep - more thorough      |
| **slotscheck**         | `__slots__` validation | None                 | Keep (currently disabled) |
| **taplo**              | TOML lint/format       | None                 | Keep                      |
| **typos**              | Spell checking         | None                 | Keep                      |
| **actionlint**         | GitHub Actions         | None                 | Keep                      |
| **validate-pyproject** | pyproject.toml         | Minor taplo overlap  | Keep                      |
| **google-yamlfmt**     | YAML formatting        | None                 | Keep (currently disabled) |

### Testing

| Tool                     | Purpose            | Decision                  |
| ------------------------ | ------------------ | ------------------------- |
| **pytest**               | Test framework     | Keep                      |
| **pytest-xdist**         | Parallel execution | Keep                      |
| **pytest-mock**          | Mocking            | Keep                      |
| **pytest-dependency**    | Test ordering      | Keep - intentional design |
| **pytest-rerunfailures** | Retry flaky tests  | Keep - network operations |
| **coverage**             | Code coverage      | Keep                      |

**Note on pytest-dependency**: Tests intentionally depend on each other. For example, `test_list` requires `test_update` to have cloned the cookbook repository. This is a conscious choice for integration-style testing, not a code smell.

### Task Running

| Tool           | Purpose                 | Decision                  |
| -------------- | ----------------------- | ------------------------- |
| **tox**        | Multi-env orchestration | Keep                      |
| **poethepoet** | Task shortcuts          | Keep - convenient aliases |
| **pre-commit** | Git hooks               | Keep                      |

## Consequences

### Positive

- Comprehensive code quality coverage from multiple perspectives
- Defense-in-depth catches issues that single tools miss
- Clear documentation of intentional design choices

### Negative

- Longer CI runs (mitigated by Python 3.14-only reducing test matrix)
- More dependencies to maintain
- Potential for conflicting tool recommendations

### Neutral

- Developers need familiarity with multiple tools
- Tool configurations spread across pyproject.toml sections

## Tool Comparison Reference

### Type Checkers Deep Dive

```
                    mypy        pyright     ty          pyrefly
Speed               Slow        Fast        Very Fast   Fast
Maturity            Mature      Mature      Alpha       New
Ecosystem           Best        Good        Growing     Limited
Strictness          Config      Very Strict Strict      Moderate
VS Code             Plugin      Native      Plugin      Plugin
Maintained by       Python      Microsoft   Astral      Meta
```

### Why Not Consolidate?

We considered reducing to 1-2 type checkers but found:

1. Each catches ~5-10% unique issues the others miss
2. CI time saved is minimal (type checking is fast)
3. The cost of a shipped bug exceeds the cost of running extra tools

## References

- [JOURNAL.md](../../JOURNAL.md) - Development journal with decision timeline
- [Python 3.14 Release Notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [Astral ty announcement](https://astral.sh/blog/ty)
