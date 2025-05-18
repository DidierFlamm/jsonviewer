#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON Viewer with Textual TUI or Rich Console fallback.

Displays JSON files as collapsible, color-coded trees in terminal UI,
or prints colored tree in console for interactive environments.

Author: did
Created: Sat May 17 2025
"""


import os
import sys
from .utils import load_json
from typing import Any, Optional
from rich.tree import Tree as RichTree
from rich.text import Text
from rich.console import Console
from textual.app import App, ComposeResult
from textual.widgets import Tree, Header, Footer


        
def format_value(value: Any, output: str) -> Text:
    """Return styled Text for given value depending on output mode ('console' or 'tui')."""
    if isinstance(value, bool):
        style = "magenta" if output == "console" else "blue"
        return Text(str(value), style=style)
    elif value is None:
        return Text("null", style="red")
    elif isinstance(value, (int, float)):
        return Text(str(value), style="cyan")
    elif isinstance(value, str):
        return Text(value, style="green")
    elif isinstance(value, bytes):
        return Text(f"bytes({len(value)})", style="italic")
    else:
        return Text(str(value))



def render_tree(node: Any, data: Any, output: str) -> None:
    """
    Recursively build a tree from JSON-like data with styled nodes and leaves.

    Args:
        node: Current tree node to populate.
        data: JSON-like data (dict, list, or primitive).
        output: 'console' or 'tui' for styling choice through format_value().
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                child = node.add(Text(f"📁 {key}", style="yellow"))
                render_tree(child, value, output)
            elif isinstance(value, list):
                child = node.add(Text(f"📋 {key}", style="yellow"))
                render_tree(child, value, output)
            else:
                leaf = Text()
                leaf.append(f"{key}: ", style="default")
                leaf.append(format_value(value, output))
                node.add(leaf)

    elif isinstance(data, list):
        for idx, item in enumerate(data):
            if isinstance(item, dict):
                child = node.add(Text(f"📁 [{idx}]", style="white"))
                render_tree(child, item, output)
            elif isinstance(item, list):
                child = node.add(Text(f"📋 [{idx}]", style="white"))
                render_tree(child, item, output)
            else:
                leaf = Text()
                leaf.append(f"[{idx}]: ", style="default")
                leaf.append(format_value(item, output))
                node.add(leaf)

    else:
        node.label = format_value(data, output)



class JSONViewer(App):
    """Textual app displaying JSON files as collapsible color-coded trees."""
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(self, file_path: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.file_path = file_path
        self.filename = None

    def compose(self) -> ComposeResult:
        """Create and yield UI widgets."""
        yield Header(show_clock=True)
        #Initialize label without filename
        label = Text("🌳 JSON", style="yellow")
        if self.filename:
            label.append(f" {self.filename}", style="default")
        yield Tree(label, id="json-tree")
        yield Footer()

    def on_mount(self) -> None:
        """Load JSON and populate tree or exit if no data."""
        data, path = load_json(self.file_path)
        if data:
            self.filename = os.path.basename(path)
            tree = self.query_one("#json-tree", Tree)
            # Update label with filename
            tree.root.label = Text("🌳 JSON ", style="yellow") + Text(self.filename, style="default")
            render_tree(tree.root, data, "tui")
            tree.root.expand()
        else:
            print("[red]No JSON file loaded. Exiting.[/red]")
            self.exit()


    
def run_console_viewer(file_path: Optional[str] = None) -> None:
    """Load JSON file and print it as a colored tree in the console."""
    console = Console()
    data, path = load_json(file_path)

    if not data:
        console.print("[red]No file selected or loaded.[/red]")
        return

    filename = os.path.basename(path)
    root_label = Text("🌳 JSON ", style="yellow") + Text(f"{filename}", style="default")

    root = RichTree(root_label)
    render_tree(root, data, "console")
    console.print(root)
    
    

def is_interactive() -> bool:
    """Detect if running inside an interactive environment (Jupyter, Spyder, VSCode)."""
    return any(mod in sys.modules for mod in ("ipykernel", "spyder", "ptpython"))

def view_json(file_path: Optional[str] = None, mode: str = "auto") -> None:
    """
    View JSON either in TUI or console depending on mode.

    Args:
        file_path: Optional path to a JSON file.
        mode: One of "auto", "console", or "tui".
              "auto": decide based on interactive environment.
              "console": force console tree display.
              "tui": force Textual interface.
    """
    if mode == "console" or (mode == "auto" and is_interactive()):
        run_console_viewer(file_path)
    else:
        JSONViewer(file_path=file_path).run()


    
    
__all__ = ["view_json",
           "JSONViewer",
           "run_console_viewer",
           ]
