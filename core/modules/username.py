import requests
from rich.console import Console
from rich.table import Table
from platforms import PLATFORMS

console = Console()

def main(target):
    table = Table(title=f"Username Scan : {target}")
    table.add_column("Platform", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("URL", style="blue")

    for platform, data in PLATFORMS.items():
        try:
            url = data["url"].format(target)
            r = requests.get(url, timeout=6, allow_redirects=True)

            if r.status_code == 200 and data.get("error", "") not in r.text:
                table.add_row(
                    platform,
                    "[green]FOUND[/green]",
                    url
                )
            else:
                table.add_row(
                    platform,
                    "[red]NOT FOUND[/red]",
                    "-"
                )

        except Exception:
            table.add_row(
                platform,
                "[yellow]ERROR[/yellow]",
                "-"
            )

    console.print(table)
