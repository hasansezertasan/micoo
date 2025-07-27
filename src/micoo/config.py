"""Python module for micoo configuration and paths."""

from pathlib import Path

from platformdirs import PlatformDirs

dirs: PlatformDirs = PlatformDirs(
    appname="micoo",
    appauthor=False,
    version=None,
    roaming=False,
    ensure_exists=True,
)
"""Platform-specific directories for the application."""
repository_path: Path = dirs.user_cache_path / "mise-cookbooks"
"""Path to the local repository of Mise cookbooks."""
log_file_path: Path = dirs.user_log_path / "micoo.log"
"""Path to the log file."""
cookbooks_repository_url: str = "https://github.com/hasansezertasan/mise-cookbooks"
"""URL of the remote repository of Mise cookbooks."""
micoo_repository_url: str = "https://github.com/hasansezertasan/micoo"
"""URL of the remote repository of micoo."""
file_extension: str = ".mise.toml"
"""File extension for globing cookbooks."""
