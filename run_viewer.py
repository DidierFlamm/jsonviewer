#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 12:52:01 2025

@author: did
"""

from jsonviewer import view_json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Chemin vers le fichier JSON")
    parser.add_argument("--mode", choices=["auto", "console", "tui"], default="auto", help="Mode d'affichage")
    args = parser.parse_args()

    view_json(file_path=args.file, mode=args.mode)

if __name__ == "__main__":
    main()