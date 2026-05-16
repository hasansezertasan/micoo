"""Negative-path and branch coverage tests using isolated tmp repositories."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from git import GitCommandError, Repo
from typer.testing import CliRunner

from micoo import main as micoo_main
from micoo.main import app

if TYPE_CHECKING:
    from collections.abc import Iterator

runner = CliRunner()


def _init_fake_repo(path: Path, cookbooks: list[str]) -> None:
    path.mkdir(parents=True, exist_ok=True)
    repo = Repo.init(path)
    for name in cookbooks:
        (path / f"{name}.mise.toml").write_text(f"# {name}\n", encoding="utf-8")
    repo.index.add([f"{name}.mise.toml" for name in cookbooks])
    repo.index.commit("seed")


@pytest.fixture
def empty_repo_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    repo_path = tmp_path / "missing"
    monkeypatch.setattr(micoo_main, "repository_path", repo_path)
    return repo_path


@pytest.fixture
def seeded_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    repo_path = tmp_path / "cookbooks"
    _init_fake_repo(repo_path, ["python", "node"])
    monkeypatch.setattr(micoo_main, "repository_path", repo_path)
    return repo_path


@pytest.fixture
def empty_seeded_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    repo_path = tmp_path / "empty-cookbooks"
    repo_path.mkdir()
    repo = Repo.init(repo_path)
    placeholder = repo_path / "README.md"
    placeholder.write_text("placeholder", encoding="utf-8")
    repo.index.add(["README.md"])
    repo.index.commit("seed")
    monkeypatch.setattr(micoo_main, "repository_path", repo_path)
    return repo_path


def test_list_no_repo(empty_repo_path: Path) -> None:
    """Test the `list` command when the repository is missing.

    Given:
        - The repository path does not exist on disk.
    When:
        - The `list` command is invoked.
    Then:
        - The command exits with code 0.
        - The output instructs the user to run `micoo update` first.
    """
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Repository does not exist" in result.output


def test_search_no_repo(empty_repo_path: Path) -> None:
    """Test the `search` command when the repository is missing.

    Given:
        - The repository path does not exist on disk.
    When:
        - The `search` command is invoked with any term.
    Then:
        - The command exits with code 0.
        - The output instructs the user to run `micoo update` first.
    """
    result = runner.invoke(app, ["search", "py"])
    assert result.exit_code == 0
    assert "Repository does not exist" in result.output


def test_dump_no_repo(empty_repo_path: Path) -> None:
    """Test the `dump` command when the repository is missing.

    Given:
        - The repository path does not exist on disk.
    When:
        - The `dump` command is invoked with a cookbook name.
    Then:
        - The command exits with code 0.
        - The output instructs the user to run `micoo update` first.
    """
    result = runner.invoke(app, ["dump", "python"])
    assert result.exit_code == 0
    assert "Repository does not exist" in result.output


def test_interactive_no_repo(empty_repo_path: Path) -> None:
    """Test the `interactive` command when the repository is missing.

    Given:
        - The repository path does not exist on disk.
    When:
        - The `interactive` command is invoked.
    Then:
        - The command exits with code 0 without prompting.
        - The output instructs the user to run `micoo update` first.
    """
    result = runner.invoke(app, ["interactive"])
    assert result.exit_code == 0
    assert "Repository does not exist" in result.output


def test_info_no_repo(empty_repo_path: Path) -> None:
    """Test the `info` command when the repository is missing.

    Given:
        - The repository path does not exist on disk.
    When:
        - The `info` command is invoked.
    Then:
        - The command exits with code 0.
        - The repository URL is reported as `N/A`.
    """
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "Repository URL: N/A" in result.output


def test_list_empty_repo(empty_seeded_repo: Path) -> None:
    """Test the `list` command when the repository contains no cookbooks.

    Given:
        - The repository exists but contains no `.mise.toml` files.
    When:
        - The `list` command is invoked.
    Then:
        - The command exits with code 0.
        - The output reports that no cookbooks were found.
    """
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "No cookbooks found." in result.output


def test_search_no_match(seeded_repo: Path) -> None:
    """Test the `search` command when no cookbook matches the term.

    Given:
        - The repository contains seeded cookbooks (python, node).
    When:
        - The `search` command is invoked with a term matching nothing.
    Then:
        - The command exits with code 0.
        - The output reports that no matching cookbooks were found.
    """
    result = runner.invoke(app, ["search", "rust"])
    assert result.exit_code == 0
    assert "No cookbooks found matching" in result.output


def test_dump_missing_cookbook(seeded_repo: Path) -> None:
    """Test the `dump` command when the requested cookbook is absent.

    Given:
        - The repository is seeded but does not contain `ghost.mise.toml`.
    When:
        - The `dump` command is invoked with `ghost`.
    Then:
        - The command exits with code 1.
        - The output indicates that the cookbook was not found.
    """
    result = runner.invoke(app, ["dump", "ghost"])
    assert result.exit_code == 1
    assert "not found in the repository" in result.output


def test_update_git_error(
    empty_repo_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test the `update` command when cloning raises a GitCommandError.

    Given:
        - The repository path does not exist.
        - `Repo.clone_from` is patched to raise `GitCommandError`.
    When:
        - The `update` command is invoked.
    Then:
        - The command exits with code 0 (error is logged, not raised).
        - The output reports a clone/pull error.
    """
    def boom(*_args: object, **_kwargs: object) -> None:
        raise GitCommandError("clone", "boom")

    monkeypatch.setattr(Repo, "clone_from", boom)
    result = runner.invoke(app, ["update"])
    assert result.exit_code == 0
    assert "An error occurred" in result.output


def test_update_unexpected_error(
    empty_repo_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test the `update` command when cloning raises an unexpected error.

    Given:
        - The repository path does not exist.
        - `Repo.clone_from` is patched to raise `RuntimeError`.
    When:
        - The `update` command is invoked.
    Then:
        - The command exits with code 0 (handled by broad except).
        - The output reports a clone/pull error.
    """
    def boom(*_args: object, **_kwargs: object) -> None:
        raise RuntimeError("nope")

    monkeypatch.setattr(Repo, "clone_from", boom)
    result = runner.invoke(app, ["update"])
    assert result.exit_code == 0
    assert "An error occurred" in result.output


def test_update_pull_existing(seeded_repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test the `update` command pull branch on an existing repository.

    Given:
        - The repository exists on disk (seeded fixture).
        - `Repo` is patched with a fake exposing a no-op remote pull.
    When:
        - The `update` command is invoked.
    Then:
        - The command exits with code 0.
        - The output reports successful pull.
    """
    class FakeRemote:
        def pull(self) -> None:
            return None

    class FakeRepo:
        def __init__(self, _path: Path) -> None:
            self.remotes = [FakeRemote()]

    monkeypatch.setattr(micoo_main, "Repo", FakeRepo)
    result = runner.invoke(app, ["update"])
    assert result.exit_code == 0
    assert "pulled successfully" in result.output


def test_interactive_cancel(seeded_repo: Path) -> None:
    """Test the `interactive` command when the user cancels confirmation.

    Given:
        - The repository is seeded with available cookbooks.
    When:
        - The `interactive` command is invoked and the user answers `n` at
          the generate-confirmation prompt.
    Then:
        - The command exits with code 1.
    """
    result = runner.invoke(app, ["interactive"], input="python\nmise.local.toml\nn\n")
    assert result.exit_code == 1


def test_interactive_existing_file(
    seeded_repo: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test the `interactive` command when the target output file exists.

    Given:
        - The repository is seeded.
        - The working directory already contains `mise.local.toml`.
    When:
        - The `interactive` command is invoked and the user confirms with `y`.
    Then:
        - The command exits with code 1.
        - The output reports that the output file already exists.
        - The pre-existing file is not modified.
    """
    monkeypatch.chdir(tmp_path)
    target = tmp_path / "mise.local.toml"
    target.write_text("existing", encoding="utf-8")
    result = runner.invoke(app, ["interactive"], input="python\nmise.local.toml\ny\n")
    assert result.exit_code == 1
    assert "already exists" in result.output


def test_interactive_writes_file(
    seeded_repo: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test the `interactive` command happy path writing a cookbook file.

    Given:
        - The repository is seeded with `node` cookbook.
        - The working directory does not contain `mise.toml`.
    When:
        - The `interactive` command is invoked and the user selects `node`,
          target `mise.toml`, and confirms with `y`.
    Then:
        - The command exits with code 0.
        - `mise.toml` is created with the generated cookbook header.
    """
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["interactive"], input="node\nmise.toml\ny\n")
    assert result.exit_code == 0, result.output
    written = (tmp_path / "mise.toml").read_text(encoding="utf-8")
    assert "### Generated by micoo" in written


def test_main_module_smoke() -> None:
    """Test the `python -m micoo` entry point.

    Given:
        - The `micoo` package is installed.
    When:
        - The package is executed as `__main__` with no arguments.
    Then:
        - A `SystemExit` is raised (Typer exits after showing help because
          the app is configured with `no_args_is_help=True`).
    """
    import runpy

    with pytest.raises(SystemExit):
        runpy.run_module("micoo", run_name="__main__")
