from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    text = Text()
    text.append(" SKY ", style="bold white on blue")
    text.append(" PLUG CDM DEV\n", style="bold cyan")
    text.append("SkyPlug-Intel OSINT Framework\n", style="white")
    text.append("Developer : Sky Plug CDM\n", style="green")
    text.append("OSINT • Legal Use Only the creation CDM", style="dim")

    console.print(Panel(text, border_style="cyan", expand=False))
