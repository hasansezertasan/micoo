"""Smoke tests for CLI commands that don't require a populated repository."""

from typer.testing import CliRunner

from micoo.main import app

runner = CliRunner()


def test_help() -> None:
    """Test the application help output.

    Given:
        - The Typer app is registered.
    When:
        - The CLI is invoked with `--help`.
    Then:
        - The command exits with code 0.
        - The output contains the application name banner.
    """
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "micoo" in result.output


def test_version() -> None:
    """Test the `version` command of the application.

    Given:
        - The `micoo` distribution metadata is installed.
    When:
        - The `version` command is invoked.
    Then:
        - The command exits with code 0.
    """
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0, result.output


def test_root() -> None:
    """Test the `root` command of the application.

    Given:
        - The `root` command echoes the repository path constant.
    When:
        - The `root` command is invoked.
    Then:
        - The command exits with code 0.
    """
    result = runner.invoke(app, ["root"])
    assert result.exit_code == 0, result.output


def test_log() -> None:
    """Test the `log` command of the application.

    Given:
        - The `log` command echoes the log file path constant.
    When:
        - The `log` command is invoked.
    Then:
        - The command exits with code 0.
    """
    result = runner.invoke(app, ["log"])
    assert result.exit_code == 0, result.output


def test_remote() -> None:
    """Test the `remote` command of the application.

    Given:
        - The `remote` command echoes the cookbooks repository URL constant.
    When:
        - The `remote` command is invoked.
    Then:
        - The command exits with code 0.
    """
    result = runner.invoke(app, ["remote"])
    assert result.exit_code == 0, result.output


def test_info() -> None:
    """Test the `info` command of the application.

    Given:
        - The application reports version, python, platform, and paths.
    When:
        - The `info` command is invoked.
    Then:
        - The command exits with code 0.
        - The output contains the Application Version line.
    """
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0, result.output
    assert "Application Version:" in result.output
