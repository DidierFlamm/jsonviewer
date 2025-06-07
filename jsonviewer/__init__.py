#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jsonviewer package initialization.

Ce package fournit des outils pour visualiser, charger et sauvegarder
des fichiers JSON, avec une interface graphique et un mode console.

Modules exposés :
- viewer : fonctions et classes pour afficher les JSON (view_json, JSONViewer, run_console_viewer)
- utils  : utilitaires pour charger et sauvegarder des fichiers JSON (load_json, save_json)


Created on Sun May 18 12:36:58 2025

@author: did
"""



from .viewer import view_json, JSONViewer, run_console_viewer
from .utils import save_json, load_json

__all__ = [
    "view_json",
    "JSONViewer",
    "run_console_viewer",
    "save_json",
    "load_json",
]