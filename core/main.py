import argparse
import sys
import os

CORE_DIR = os.path.dirname(os.path.abspath(__file__))
if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

from modules.output.main import main as output_main
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from banner import show_banner

console = Console()

def banner():
    text = Text()
    text.append("PLUG CDM Dev\n", style="bold cyan")
    text.append("SkyPlug-Intel OSINT Framework\n", style="bold white")
    text.append("Developer : Plug CDM\n", style="green")
    text.append("OSINT • Legal Use Only", style="dim")

    console.print(Panel(text, expand=False, border_style="cyan"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-m", "--module", required=True)
    args = parser.parse_args()

    output_main(args)

if __name__ == "__main__":
    main()

