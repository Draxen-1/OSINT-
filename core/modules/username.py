import requests
from rich.table import Table
from rich.console import Console
from platforms import PLATFORMS

console = Console()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

TIMEOUT = 7


def check_username(platform, url_pattern, username):
    try:
        url = url_pattern.format(username)
    except Exception:
        return "ERROR", None

    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            allow_redirects=True
        )

        if r.status_code in (200, 301, 302, 403):
            return "FOUND", url
        if r.status_code == 404:
            return "NOT FOUND", None

        return "NOT FOUND", None

    except requests.exceptions.RequestException:
        return "ERROR", None

       

def main(target):
    table = Table(title=f"Username Scan : {target}")

    table.add_column("Platform", style="cyan", no_wrap=True)
    table.add_column("Status", style="bold")
    table.add_column("URL", style="green")

    for platform, pattern in PLATFORMS.items():
        status, url = check_username(platform, pattern, target)

        if status == "FOUND":
            table.add_row(platform, "[green]FOUND[/green]", url)
        elif status == "NOT FOUND":
            table.add_row(platform, "[red]NOT FOUND[/red]", "-")
        else:
            table.add_row(platform, "[yellow]ERROR[/yellow]", "-")

    console.print(table)

