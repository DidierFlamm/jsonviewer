#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:30:32 2025

@author: did
"""

import os
import json
import datetime
from tkinter import Tk, filedialog
from typing import Any, Optional, Tuple

def save_json(
    variable: Any,
    file_name: str,
    folder_path: Optional[str] = None,
    time_stamp: bool = False
) -> str:
    """
    Sauvegarde une variable Python (dict, list, etc.) dans un fichier JSON.

    Args:
        variable: Objet Python à enregistrer (ex: dict, list…)
        file_name: Nom de base du fichier (sans extension)
        folder_path: Dossier de destination (par défaut: dossier courant)
        time_stamp: Ajoute un timestamp au nom du fichier si True

    Returns:
        Chemin complet du fichier créé
    """
    # Ajoute timestamp si demandé
    if time_stamp:
        timestamp = datetime.datetime.now().isoformat(timespec='seconds').replace(":", "-")
        file_name = f"{file_name}_{timestamp}"

    # Ajoute extension .json si absente
    if not file_name.endswith(".json"):
        file_name += ".json"

    # Dossier de destination (par défaut: courant)
    if folder_path is None:
        folder_path = "."

    os.makedirs(folder_path, exist_ok=True)
    filepath = os.path.join(folder_path, file_name)

    # Sauvegarde au format JSON
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(variable, f, indent=2, ensure_ascii=False)

    print(f"✅ Fichier JSON sauvegardé : {filepath}")
    return filepath


def load_json(file_path: Optional[str] = None) -> Tuple[Optional[Any], Optional[str]]:
    """
    Load JSON from a given file path or via a file dialog if None.

    Returns:
        Tuple of (parsed data or None, file path or None)
    """
    if file_path and os.path.isfile(file_path):
        path = file_path
    else:
        root = Tk()
        root.withdraw()  # Ne pas afficher la fenêtre principale
        path = filedialog.askopenfilename(
            title="Choose JSON file",
            filetypes=[("JSON files", "*.json")],
        )
        root.destroy()

    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f), path
        except Exception as e:
            print(f"[red]Error loading JSON file {path}: {e}[/red]")
            return None, None
    return None, None


__all__ = [
    "save_json",
    "load_json",
]