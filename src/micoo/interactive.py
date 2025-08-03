"""Interactive mode for micoo cookbook selection."""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from micoo.config import file_extension, repository_path
from micoo.logging_setup import logger

console = Console()


class InteractiveMode:
    """Interactive mode for cookbook selection and management."""

    def __init__(self) -> None:
        """Initialize the interactive mode."""
        self.console = console

    def show_welcome(self) -> None:
        """Display welcome message."""
        welcome_text = Text("Welcome to micoo interactive mode!", style="bold blue")
        subtitle = Text("Select and manage your mise cookbooks", style="italic")

        panel = Panel(f"{welcome_text}\n{subtitle}", title="micoo", border_style="blue")
        self.console.print(panel)

    @staticmethod
    def get_available_cookbooks() -> List[str]:
        """Get list of available cookbooks.

        Returns:
            List of cookbook names
        """
        if not repository_path.exists():
            return []

        cookbooks = [
            cookbook
            for cookbook in repository_path.rglob(pattern=f"*{file_extension}")
            if cookbook.is_file()
        ]
        return sorted([cookbook.name[: -len(file_extension)] for cookbook in cookbooks])

    def select_cookbook(self, cookbooks: List[str]) -> Optional[str]:
        """Let user select a cookbook.

        Args:
            cookbooks: List of available cookbooks

        Returns:
            Selected cookbook name or None if cancelled
        """
        if not cookbooks:
            self.console.print(
                "[red]No cookbooks available. Please run 'micoo update' first.[/red]"
            )
            return None

        questions = [
            inquirer.List(
                "cookbook",
                message="Select a cookbook",
                choices=cookbooks,
                carousel=True,
            )
        ]

        try:
            answers = inquirer.prompt(questions)
        except (KeyboardInterrupt, EOFError):
            self.console.print("[yellow]Prompt cancelled by user.[/yellow]")
            msg = "Prompt cancelled by user."
            logger.info(msg)
            return None

        return answers.get("cookbook") if answers else None

    def confirm_action(self, cookbook_name: str, output_file: str) -> bool:  # noqa: PLR6301
        """Confirm the action with user.

        Args:
            cookbook_name: Selected cookbook name
            output_file: Output file path

        Returns:
            True if user confirms, False otherwise
        """
        questions = [
            inquirer.Confirm(
                "confirm",
                message=f"Generate {cookbook_name} cookbook to {output_file}?",
                default=True,
            )
        ]

        answers = inquirer.prompt(questions)
        return answers.get("confirm", False) if answers else False

    def select_output_location(self) -> str:
        """Let user select the output file location.

        Returns:
            Selected output file path
        """
        output_options = [
            ("mise.toml", "Standard configuration file"),
            ("mise.local.toml", "Local config (not committed to source control)"),
            ("mise/config.toml", "Configuration in mise subdirectory"),
            (".config/mise.toml", "Configuration in .config directory"),
            (".config/mise/config.toml", "Configuration in .config/mise subdirectory"),
            (
                ".config/mise/conf.d/custom.toml",
                "Configuration in conf.d directory (alphabetical loading)",
            ),
        ]

        questions = [
            inquirer.List(
                "output_location",
                message="Select output file location",
                choices=[f"{path} - {desc}" for path, desc in output_options],
                carousel=True,
            )
        ]

        answers = inquirer.prompt(questions)
        selected = answers.get("output_location") if answers else None
        if not selected:
            self.console.print("[yellow]No output location selected. Exiting.[/yellow]")
            msg = "No output location selected. Exiting."
            logger.info(msg)
            return None

        # Extract just the path part
        return selected.split(" - ")[0]

    def generate_cookbook(self, cookbook_name: str, output_file: str) -> bool:
        """Generate a cookbook to the specified output file.

        Args:
            cookbook_name: Name of the cookbook to generate
            output_file: Output file path

        Returns:
            True if successful, False otherwise
        """
        cookbook_path = repository_path / (cookbook_name + file_extension)
        if not cookbook_path.exists():
            self.console.print(f"[red]Cookbook '{cookbook_name}' not found.[/red]")
            msg = f"Cookbook '{cookbook_name}' not found in the repository."
            logger.error(msg)
            return False

        # Read the cookbook content
        with cookbook_path.open(encoding="utf-8") as f:
            content = f.read()

        # Write to output file
        output_path = Path(output_file)

        # Create parent directories if they don't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as f:
            f.write(content)
        return True

    def show_success(self, cookbook_name: str, output_file: str) -> None:
        """Show success message.

        Args:
            cookbook_name: Generated cookbook name
            output_file: Output file path
        """
        success_text = Text(
            f"✅ Successfully generated {cookbook_name} cookbook!", style="bold green"
        )
        file_text = Text(f"Output: {output_file}", style="blue")

        panel = Panel(
            f"{success_text}\n{file_text}", title="Success", border_style="green"
        )
        self.console.print(panel)

    def run_interactive_mode(self) -> None:
        """Run the interactive mode."""
        msg = "Starting interactive mode"
        logger.info(msg)

        self.show_welcome()

        # Get available cookbooks
        cookbooks = InteractiveMode.get_available_cookbooks()

        if not cookbooks:
            self.console.print(
                "[red]No cookbooks found. Please run 'micoo update' first.[/red]"
            )
            return

        # Select cookbook
        selected_cookbook = self.select_cookbook(cookbooks)
        if not selected_cookbook:
            self.console.print("[yellow]No cookbook selected. Exiting.[/yellow]")
            return

        msg = f"Cookbook '{selected_cookbook}' selected"
        logger.info(msg)

        # Confirm action
        output_file = self.select_output_location()
        if not self.confirm_action(selected_cookbook, output_file):
            self.console.print("[yellow]Action cancelled.[/yellow]")
            return

        # Generate the cookbook
        if self.generate_cookbook(selected_cookbook, output_file):
            self.show_success(selected_cookbook, output_file)
        else:
            self.console.print("[red]Failed to generate cookbook.[/red]")
            return

        msg = f"Successfully generated {selected_cookbook} cookbook to {output_file}"
        logger.info(msg)

        msg = "Interactive mode completed"
        logger.info(msg)
