# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- changelog-start -->

## [Unreleased]

## [0.4.0] - 2025-08-03

## :rocket: Features

- chore(release): migrate to release-drafter from release-please by @hasansezertasan in (#37)
- chore(ci): remove git-cliff configuration and update CI/CD workflows by @hasansezertasan in (#36)
- feat(dependencies): add hatch-fancy-pypi-readme and poethepoet to development dependencies by @hasansezertasan in (#33)
- feat(tests): add test for `log` command to verify successful execution and output by @hasansezertasan in (#34)
- feat(command): implemented a new command to display the path to the micoo log file by @hasansezertasan in (#31)
- feat(logging): enhance logging setup and improve command logging in main application by @hasansezertasan in (#30)
- ci(check-pr-title.yml): add pr title validation action by @hasansezertasan in (#26)
- ci(release-please): set changelog-type to github by @hasansezertasan in (#27)
- chore: tiny adjustments by @hasansezertasan in (#23)
- chore: bootstrap releases for path: . by @hasansezertasan in (#24)

## :beetle: Bug Fixes

- fix(check-pr-title): update sticky-pull-request-comment action to version 2.9.0 by @hasansezertasan in (#32)
- fix(root-command): changed output path for root command to reflect the correct repository path by @hasansezertasan in (#29)

## [0.3.0] - 2025-07-27

## :beetle: Bug Fixes

- Versioning by @hasansezertasan in (#21)

## [0.2.0] - 2025-07-27

## :rocket: Features

- Git-cliff integration by @hasansezertasan in (#6)
- Implement dynamic arguments and pin python version to 3.9 by @hasansezertasan in (#4)
- Generate release notes and discussions on gh-release, adjust permissions, bump setup-uv version by @hasansezertasan in (#3)

## :beetle: Bug Fixes

- Merge README.md and CHANGELOG.md when publishing to PyPI by @hasansezertasan in (#2)
- Correct replacement pattern in fancy-pypi-readme hook by @hasansezertasan in (#1)

## :rocket: Features

- Remove redundant configs by @hasansezertasan in (#5)

## [0.1.0] - 2025-07-27

## :rocket: Features

- Initial commit by @hasansezertasan

## New Contributors

- @hasansezertasan made their first contribution

<!-- refs -->
[unreleased]: https://github.com/hasansezertasan/micoo/compare/0.4.0..HEAD
[0.4.0]: https://github.com/hasansezertasan/micoo/compare/0.3.0..0.4.0
[0.3.0]: https://github.com/hasansezertasan/micoo/compare/0.2.0..0.3.0
[0.2.0]: https://github.com/hasansezertasan/micoo/compare/0.1.0..0.2.0

<!-- changelog-end -->
