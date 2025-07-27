# micoo: quick access to `mise-cookbooks`

<!-- TODO: Make it work, make it right, make it fast. -->

[![CI](https://github.com/hasansezertasan/micoo/actions/workflows/ci.yml/badge.svg)](https://github.com/hasansezertasan/micoo/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/micoo.svg)](https://pypi.org/project/micoo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/micoo.svg)](https://pypi.org/project/micoo)
[![License - MIT](https://img.shields.io/github/license/hasansezertasan/micoo.svg)](https://opensource.org/licenses/MIT)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/micoo)][micoo]

<!-- [![Coverage](https://codecov.io/gh/hasansezertasan/micoo/graph/badge.svg?token=XXXXXXXXXXX)](https://codecov.io/gh/hasansezertasan/micoo) -->

<!-- [![Coverage](https://img.shields.io/codecov/c/github/hasansezertasan/micoo)](https://codecov.io/gh/hasansezertasan/micoo) -->

<!-- [![Coverage](https://codecov.io/gh/hasansezertasan/micoo/branch/main/graph/badge.svg)](https://codecov.io/gh/hasansezertasan/micoo) -->

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![GitHub Tag](https://img.shields.io/github/tag/hasansezertasan/micoo?include_prereleases=&sort=semver&color=black)](https://github.com/hasansezertasan/micoo/releases/)

[![Downloads](https://pepy.tech/badge/micoo)](https://pepy.tech/project/micoo)
[![Downloads/Month](https://pepy.tech/badge/micoo/month)](https://pepy.tech/project/micoo)
[![Downloads/Week](https://pepy.tech/badge/micoo/week)](https://pepy.tech/project/micoo)

`micoo` (short for **mise cookbooks**) is a :zap: command-line tool that makes it easy to access [mise] configuration files from [mise-cookbooks] :books:.

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
╭─ Options ─────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.               │
│ --show-completion             Show completion for the current shell, to copy it or    │
│                               customize the installation.                             │
│ --help                        Show this message and exit.                             │
╰───────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────╮
│ update    Clone or fetch the `mise-cookbooks` repository.                             │
│ list      List the available mise cookbooks.                                          │
│ search    Search for a mise cookbook.                                                 │
│ dump      Dump a mise cookbook.                                                       │
│ root      Show the path to the micoo boilerplates directory.                          │
│ remote    Show the URL to the remote repository.                                      │
│ version   Show the current version number of micoo.                                   │
│ info      Display information about the micoo application.                            │
╰───────────────────────────────────────────────────────────────────────────────────────╯
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

Open the [mise-cookbooks] repository in the browser:

```sh
open $(micoo remote)
```

Open the cloned repository in the file manager:

```sh
open $(micoo root)
```

Show the current version of `micoo`:

```sh
micoo version
```

Show the information about the `micoo` application:

```sh
micoo info
```

## Support :heart:

If you have any questions or need help, feel free to open an issue on the [GitHub repository][micoo].

## Author :person_with_crown:

This project is maintained by [Hasan Sezer Taşan][author], It's me :wave:

## Contributing :heart:

Any contributions are welcome! Please follow the [Contributing Guidelines](./CONTRIBUTING.md) to contribute to this project.

## Development :toolbox:

To set up the development environment:

```sh
# Clone the repository
git clone https://github.com/hasansezertasan/micoo.git
cd micoo

# Install development dependencies
uv sync

# Update the code...

# Run tests
uv run --locked tox run

# Add a new git tag.
git tag -a 0.3.0 a71e27a -m "bump: version 0.2.0 → 0.3.0"
git push origin tag 0.3.0

# Build the package
uv build
```

## Related Projects :chains:

- [mise] - The official mise project
- [mise-cookbooks] - Collection of mise cookbooks

## License :scroll:

This project is licensed under the [MIT License](https://opensource.org/license/MIT).

<!-- Refs -->
[mise-cookbooks]: https://github.com/hasansezertasan/mise-cookbooks
[mise]: https://github.com/jdx/mise
[author]: https://github.com/hasansezertasan
[micoo]: https://github.com/hasansezertasan/micoo

## Changelog :memo:

For a detailed list of changes, please refer to the [CHANGELOG](./CHANGELOG.md).
