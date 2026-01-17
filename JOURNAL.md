# Development Journal

Chronological record of decisions, attempts (including failures), and outcomes for the micoo project.

---

## 2026-01-17: Python Version Decision

### Context

Evaluating which Python versions to support for a CLI tool distributed via pipx, uvx, and Homebrew tap.

### Options Considered

| Option             | Pros                                      | Cons                                                      |
| ------------------ | ----------------------------------------- | --------------------------------------------------------- |
| **3.8+** (current) | Maximum compatibility                     | 3.8 EOL (Oct 2024), 3.9 EOL (Oct 2025), large test matrix |
| **3.10+**          | Modern features (match, union syntax)     | Still 5 versions to test                                  |
| **3.13+**          | Recent, proven stable                     | 2 versions to test                                        |
| **3.14+ only**     | Simplest, all latest features, minimal CI | May exclude users on older systems                        |

### Decision

**Python 3.14+ only**

### Rationale

1. **CLI distribution methods handle Python**: pipx, uvx, and Homebrew can all provide Python 3.14 automatically - users aren't constrained by pre-installed versions
2. **Simplified maintenance**: Single version means no compatibility shims, no conditional imports, no version-specific workarounds
3. **Latest language features**: Full access to Python 3.14 features without `from __future__` imports or version checks
4. **Faster CI**: Testing one version instead of six reduces CI time and complexity
5. **Forward-looking**: As a new CLI tool, targeting the latest stable ensures longevity

### Trade-offs Accepted

- Users on restricted systems may need to upgrade or use a Python version manager
- Some enterprise environments may not have 3.14 available immediately
- Dependencies must support 3.14 (most modern packages do)

### Related

- See [ADR-001: Development Tooling](docs/adr/001-development-tooling.md) for tooling decisions

---

## 2026-01-17: Development Tooling Audit

### Context

Reviewed all development tools in pyproject.toml to assess overlap and necessity.

### Decision

**Keep all current tools** - the redundancy provides value through different perspectives.

### Rationale

#### Type Checkers (4 tools: mypy, pyright, ty, pyrefly)

Each catches different issues:

- **mypy**: De-facto standard, best ecosystem compatibility
- **pyright**: Stricter in some areas, excellent VS Code integration
- **ty**: Rust-based (Astral team), extremely fast, future direction
- **pyrefly**: Different analysis approach (Meta)

Running multiple type checkers is unusual but provides defense-in-depth for a CLI tool that needs reliability.

#### Linting & Formatting

- **ruff**: Primary linter/formatter (replaces many tools)
- **vulture**: Dead code detection (ruff doesn't fully cover this)
- **taplo**: TOML-specific (necessary for pyproject.toml quality)
- **typos**: Spell checking across all files
- **actionlint**: CI workflow validation

#### Testing

- **pytest-dependency**: Tests intentionally depend on each other (e.g., `test_list` requires `test_update` to clone the repo first). This is a conscious design choice for integration-style tests.
- **pytest-rerunfailures**: Handles transient network issues when testing git operations

### Related

- See [ADR-001: Development Tooling](docs/adr/001-development-tooling.md) for full details

---

## 2026-01-17: Application Data Storage Convention

### Context

Evaluating whether to use `platformdirs` (XDG-compliant, platform-specific paths) or Unix single-folder convention (`~/.micoo/`) for storing application data.

### Options Considered

| Option                               | Pros                                                                                             | Cons                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **platformdirs** (current)           | XDG-compliant, platform-native paths, cache clearable separately, consistent with mise ecosystem | Files scattered across multiple locations                   |
| **Unix single-folder** (`~/.micoo/`) | Simple mental model, easy to nuke everything, one path to remember                               | Non-XDG, dotfile clutter, doesn't follow modern conventions |

### Decision

**Keep platformdirs**

### Rationale

1. **Ecosystem consistency**: mise itself uses XDG-compliant paths; micoo should follow the same convention
2. **Cross-platform**: Homebrew distribution means macOS users expect native paths (`~/Library/Caches/`)
3. **Cache management**: Users can clear `~/.cache/micoo/` without losing configuration
4. **Modern convention**: Modern CLI tools (uv, ruff, mise) all follow XDG Base Directory spec
5. **Already implemented**: No migration path needed

### Current Paths

```
Cache: ~/.cache/micoo/mise-cookbooks/
Logs:  ~/.local/state/micoo/log/micoo.log
```

### Trade-offs Accepted

- Users must know multiple paths (mitigated by `micoo root` and `micoo log` commands)
- Slightly more complex mental model
