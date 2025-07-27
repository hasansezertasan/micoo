---
name: Bug report
about: Report a bug in `micoo`
title: 'Bug: '
labels: bug
assignees: 'hasansezertasan'
---
# Bug Report

## Bug Description

<!--
This issue tracker is a tool to address bugs in micoo itself.
Please use GitHub Discussions about your own code or scenarios.

Replace this comment with a clear outline of what the bug is.
-->

## How to Reproduce

<!--
Describe how to replicate the bug.

Include a minimal reproducible example that demonstrates the bug. Here is an example of a minimal reproducible example:

```shell
micoo dump python
```

Include the full traceback if there was an exception. For example:

```shell
╭────────────────────────── Traceback (most recent call last) ──────────────────────────╮
│ /Users/hasansezertasan/Developer/projects/micoo/src/micoo/main.py:187 in dump         │
│                                                                                       │
│   184 │   Dump a specific cookbook to a file:                                         │
│   185 │   │   micoo dump python > .mise.toml                                          │
│   186 │   """                                                                         │
│ > 187 │   0/0                                                                         │
│   188 │   cookbook_path = repository_path / (name + file_extension)                   │
│   189 │   if not cookbook_path.exists():                                              │
│   190 │   │   typer.echo(f"Cookbook '{name}' not found.")                             │
│                                                                                       │
│ ╭──── locals ─────╮                                                                   │
│ │ name = 'python' │                                                                   │
│ ╰─────────────────╯                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────╯
ZeroDivisionError: division by zero
```
-->

## Expected Behavior

<!--
Describe the expected behavior that should have happened but didn't.
-->

## Environment

<!--
Simply run `micoo info` and paste the output here.

```shell
Application Version: 0.1.dev0+d20250726
Python Version: 3.8.20 (CPython)
Platform: Darwin
Repository Path: /Users/hasansezertasan/Library/Caches/micoo/mise-cookbooks
Repository URL: https://github.com/hasansezertasan/mise-cookbooks/tree/81747c2e983fa1278005c8cb8b0e311a7726923a
```
-->
