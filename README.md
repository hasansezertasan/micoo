# micoo: quick access to `mise-cookbooks`

> [!WARNING]
> **`micoo` is deprecated and no longer maintained.** It has been superseded by
> [`cobo`](https://github.com/hasansezertasan/cobo), a generic boilerplate
> fetcher that supports mise cookbooks, gitignore templates, and any
> user-configured source. See [**Migrating to `cobo`**](#migrating-to-cobo)
> below for the migration guide.

[![CI](https://github.com/hasansezertasan/micoo/actions/workflows/ci.yml/badge.svg)](https://github.com/hasansezertasan/micoo/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/micoo.svg)](https://pypi.org/project/micoo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/micoo.svg)](https://pypi.org/project/micoo)
[![License - MIT](https://img.shields.io/github/license/hasansezertasan/micoo.svg)](https://opensource.org/licenses/MIT)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/micoo)][micoo]

[![codecov](https://codecov.io/gh/hasansezertasan/micoo/graph/badge.svg?token=z8EzL0t2cT)](https://codecov.io/gh/hasansezertasan/micoo)

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![GitHub Tag](https://img.shields.io/github/tag/hasansezertasan/micoo?include_prereleases=&sort=semver&color=black)](https://github.com/hasansezertasan/micoo/releases/)

[![Downloads](https://pepy.tech/badge/micoo)](https://pepy.tech/project/micoo)
[![Downloads/Month](https://pepy.tech/badge/micoo/month)](https://pepy.tech/project/micoo)
[![Downloads/Week](https://pepy.tech/badge/micoo/week)](https://pepy.tech/project/micoo)

`micoo` (short for **mise cookbooks**) is a :zap: command-line tool that makes it easy to access [mise] configuration files from [mise-cookbooks] :books:.

## Migrating to `cobo`

`micoo` is no longer maintained — `v0.6.0` is the final release. Prior releases stay installable for reproducibility but receive no fixes.

### Swap the tool

```sh
uv tool uninstall micoo
uv tool install cobo
```

(Using `pipx` or `mise install pipx:micoo`? Substitute the equivalent uninstall/install commands.)

Then use it exactly as before, under the `mise` source:

```sh
cobo mise update
cobo mise dump python > mise.local.toml
```

### Command mapping

| Old (`micoo`) | New (`cobo`) |
| --- | --- |
| `micoo dump python` | `cobo mise dump python` |
| `micoo list` | `cobo mise list` |
| `micoo search foo` | `cobo mise search foo` |
| `micoo update` | `cobo mise update` (single source) or `cobo update` (all sources) |
| `micoo root` | `cobo mise root` (single source) or `cobo root` (cache root) |
| `micoo remote` | `cobo mise remote` |
| `micoo info` | `cobo info` |
| `micoo log` | *(dropped — cobo has no log command; `cobo info` reports the cache root)* |
| `micoo version` | `cobo version` |
| `micoo interactive` | *(dropped — use shell redirection: `cobo mise dump python > mise.local.toml`)* |

### Why?

`micoo` only fetched mise cookbooks. `cobo` generalizes the same pattern (`clone a repo, list templates, dump one to stdout`) to any boilerplate source — with built-in support for `mise`, `gitignore`, `gitattributes`, `editorconfig`, and `licenses`, plus user-defined sources via a single TOML config.

New issues should be filed against [cobo](https://github.com/hasansezertasan/cobo/issues) rather than this repository.

## Typical Usage :rocket:

```sh
# List available cookbooks
micoo list

# Create a new mise.toml with a cookbook
micoo dump python > mise.toml
```

## Features :sparkles:

- 🚀 Quick access to [mise-cookbooks]
- 📚 Easy cookbook listing and content viewing
- 💾 Simple dumping of cookbooks to mise.toml
- 🔄 Repository cloning and updating
- 🌐 Browser integration for quick repository access
- 🎯 Interactive mode for cookbook selection and generation

## Installation :package:

There are several ways to install `micoo`! :rocket: I recommend using (obviously) [mise] :hammer_and_wrench:. Here's how to do it:

```sh
mise install pipx:micoo
```

Alternatively, you can install it using `uv tool install micoo` :jigsaw:

```sh
uv tool install micoo
```

## Command Reference :book:

Here is the output of the `micoo --help` command:

```sh
 Usage: micoo [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                            │
│ --show-completion             Show completion for the current shell, to copy it or customize the   │
│                               installation.                                                        │
│ --help                        Show this message and exit.                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────╮
│ update        Clone or fetch the `mise-cookbooks` repository.                                      │
│ list          List the available mise cookbooks.                                                   │
│ search        Search for a mise cookbook.                                                          │
│ dump          Dump a mise cookbook.                                                                │
│ root          Show the path to the micoo boilerplates directory.                                   │
│ log           Show the path to the micoo log file.                                                 │
│ remote        Show the URL to the remote repository.                                               │
│ version       Show the current version number of micoo.                                            │
│ info          Display information about the micoo application.                                     │
│ interactive   Start interactive mode for cookbook selection and generation.                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Usage :hammer_and_wrench:

You can use the `micoo` command to interact with [mise-cookbooks]. Here are some common commands:

List all available cookbooks:

```sh
micoo list
```

This will output:

```sh
Available cookbooks:
- terraform
- python
- cpp
- pnpm
- node
- ruby-on-rails
- opentofu
```

Dump a specific cookbook to a `mise.toml` file:

```sh
micoo dump python > mise.toml
```

Open the [mise-cookbooks] repository in the default application:

```sh
open $(micoo remote)
```

Open the cloned repository in the default application:

```sh
open $(micoo root)
```

Open the log file in the default application:

```sh
open $(micoo log)
```

Show the current version of `micoo`:

```sh
micoo version
```

Show the information about the `micoo` application:

```sh
micoo info
```

Start interactive mode for cookbook selection and generation:

```sh
micoo interactive
```

The interactive mode supports multiple output locations:

- `mise.toml` - Standard configuration file
- `mise.local.toml` - Local config (not committed to source control)
- `mise/config.toml` - Configuration in mise subdirectory
- `.config/mise.toml` - Configuration in .config directory
- `.config/mise/config.toml` - Configuration in .config/mise subdirectory
- `.config/mise/conf.d/custom.toml` - Configuration in conf.d directory (alphabetical loading)

## Support :heart:

If you have any questions or need help, feel free to open an issue on the [GitHub repository][micoo].

## Author :person_with_crown:

This project is maintained by [Hasan Sezer Taşan][author], It's me :wave:

## Contributing :heart:

Any contributions are welcome! Please follow the [Contributing Guidelines](https://github.com/hasansezertasan/micoo/blob/main/CONTRIBUTING.md) to contribute to this project.

## Tasks

Clone the repository and cd into the project directory:

```sh
git clone https://github.com/hasansezertasan/micoo
cd micoo
```

The commands below can also be executed using the [xc task runner](https://xcfile.dev/), which combines the usage instructions with the actual commands. Simply run `xc`, it will pop up an interactive menu with all available tasks.

### `install`

Install the dependencies:

```sh
uv sync
```

### `style`

Run the style checks:

```sh
uv run --locked tox run -e style
```

### `ci`

Run the CI pipeline:

```sh
uv run --locked tox run
```

## Related Projects :chains:

- [mise] - The official mise project
- [mise-cookbooks] - Collection of mise cookbooks

## License :scroll:

This project is licensed under the [MIT License](https://opensource.org/license/MIT).

## Changelog :memo:

Please check the [Releases](https://github.com/hasansezertasan/micoo/releases) page for the changelog.

<!-- Refs -->
[mise-cookbooks]: https://github.com/hasansezertasan/mise-cookbooks
[mise]: https://github.com/jdx/mise
[author]: https://github.com/hasansezertasan
[micoo]: https://github.com/hasansezertasan/micoo
