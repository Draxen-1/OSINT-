#!/usr/bin/env python3

import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)
sys.path.insert(0, PROJECT_ROOT)

import argparse
import asyncio
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from core.loader import load_modules
from core.logger import log_result
from core.config import APP_NAME, VERSION, LEGAL_WARNING

console = Console()

BANNER = f"""
[cyan]
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗     ██╗   ██╗ ██████╗ 
██╔════╝██║ ██╔╝╚██╗ ██╔╝██╔══██╗██║     ██║   ██║██╔════╝ 
███████╗█████╔╝  ╚████╔╝ ██████╔╝██║     ██║   ██║██║  ███╗
╚════██║██╔═██╗   ╚██╔╝  ██╔═══╝ ██║     ██║   ██║██║   ██║
███████║██║  ██╗   ██║   ██║     ███████╗╚██████╔╝╚██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝
[/cyan]
[bold]{APP_NAME} v{VERSION}[/bold]
"""

async def run(target, modules):
    table = Table(title="SkyPlug-intel Results")
    table.add_column("Module")
    table.add_column("Result")

    results = await asyncio.gather(
        *[m.run(target) for m in modules],
        return_exceptions=True
    )

    for m, r in zip(modules, results):
        table.add_row(m.name, str(r))
        log_result(m.name, target, r)

    console.print(table)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-m", "--module")
    args = parser.parse_args()

    os.system("clear")
    console.print(Panel.fit(BANNER))
    console.print(f"[yellow]{LEGAL_WARNING}[/yellow]\n")

    modules = load_modules(args.module)
    asyncio.run(run(args.target, modules))

if __name__ == "__main__":
    main()
