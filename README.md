# 📄 JSON Viewer

Un visualiseur de fichier JSON en terminal sous forme d’arbre coloré, soit :

- dans une **interface TUI interactive** avec [Textual](https://textual.textualize.io/) (`tui`)
- soit dans le **terminal standard**, avec arbre coloré via [Rich](https://rich.readthedocs.io/) (`console`)

---

## 🚀 Installation des dépendances

```bash
pip install textual rich
```

---

## ✅ Fonctionnalités

- Ouverture de fichiers JSON depuis la ligne de commande ou via boîte de dialogue
- Affichage interactif (TUI) ou simple (console)
- Nœuds colorés selon le type : objets 📁, listes 📋, valeurs primitives
- Navigation dans l’arbre dans le mode TUI


### 💻 Utilisation comme script

```bash
python run_viewer.py -f mon_fichier.json
```
Ce script lance le visualiseur de fichier JSON.
Par défaut, en environnement interactif (Jupyter,Spyder …), le visualiseur s’affiche en console colorée. 
Sinon, c’est la TUI Textual qui se lance.

Arguments :

-f, --file : chemin d’un fichier JSON

--mode : "auto" (par défaut), "tui" ou "console"


### 👨‍💻 Utilisation comme bibliothèque

```python
from jsonviewer import view_json

view_json("chemin/vers/ton_fichier.json", mode="auto")
```

Le mode "auto" détecte l’environnement et choisit la meilleure interface.


### 📝 Signature

```python
def view_json(
    file_path: Optional[str] = None, 
    mode: str = "auto"
    ) -> None:
    """Affiche un fichier JSON dans le terminal ou via une interface TUI."""
```

## 📆 Fonctions exportées
| Fonction              | Description                                          |
|-----------------------|------------------------------------------------------|
|Fonction principales                                                          |
| view_json(...)        | Fonction principale pour afficher un JSON            |
| run_console_viewer    | Affiche l’arbre JSON dans la console Rich            |
| JSONViewer            | Classe Textual utilisée pour l’interface interactive |
|                       |                                                      |
|Fonctions utilitaires                                                         |
| save_json(...)        | Sauvegarde une variable Python dans un fichier JSON  |
| load_json(...)        | Charge un fichier JSON (via chemin ou GUI)           |
    
---

## 📋 Exemple d’arborescence console

Fichier source :

```json
{
  "name": "Alice",
  "age": 30,
  "skills": ["Python", "Data"],
  "location": {"city": "Paris", "zip": 75000}
}
```
Affichage console :
```
🌳 JSON example.json
├── name: Alice
├── age: 30
├── 📋 skills
│   ├── [0]: Python
│   └── [1]: Data
└── 📁 location
    ├── city: Paris
    └── zip: 75000
```    
---

## 🛠️ Utilitaires

### 💾 Sauvegarder une variable Python en JSON

La fonction utilitaire save_json() permet d’enregistrer facilement une variable Python (généralement un dictionnaire ou une liste)
dans un fichier .json, avec des options pratiques :

- Création automatique du dossier si nécessaire
- Ajout d’un timestamp dans le nom du fichier (utile pour les logs)
- Support de l'encodage UTF-8 et indentations lisibles

#### Signature

```python
def save_json(
    variable: Any,
    file_name: str,
    folder_path: Optional[str] = None,
    time_stamp: bool = False
) -> str:
    """Sauvegarde une variable Python dans un fichier JSON formaté et retourne le chemin créé."""
```

#### Exemple

```python
from jsonviewer import save_json

data = {
    "user": "Alice",
    "score": 42,
    "date": "2025-05-18"
}

# Sauvegarde dans le dossier "logs" avec horodatage
save_json(data, "my_data", folder_path="logs", time_stamp=True)

# Cela créera un fichier comme :
# logs/my_data_2025-05-18T16-22-05.json
```

---

### 📂 Charger un fichier JSON

La fonction utilitaire load_json() permet de charger facilement un fichier JSON depuis un chemin donné.
Si aucun chemin n’est fourni, elle ouvre une boîte de dialogue pour choisir un fichier.

#### Signature

```python
def load_json(file_path: Optional[str] = None
) -> Tuple[Optional[Any], Optional[str]]:
    """
    Charge un fichier JSON depuis un chemin donné ou via une boîte de dialogue si None.
    Retourne un tuple : (données JSON chargées ou None, chemin du fichier ou None).
    """
```

#### Exemple

```python
data, path = load_json()  # ouvre une boîte de dialogue si aucun chemin fourni
if data is not None:
    print(f"Fichier chargé : {path}")
```

---

## 🧰 Organisation du code

Le package contient :
```
jsonviewer/
├── run_viewer.py      # Script de lancement
└── jsonviewer/
    ├── __init__.py    # Import simplifié des fonctions clés
    ├── viewer.py      # Visualiseur TUI et console, fonction view_json
    └── utils.py       # Fonction save_json et load_json
```

L'import est facilité grâce au fichier __init__ :

```python
from jsonviewer import view_json, save_json
```

---

## 📜 License

MIT License

---

## 📝 Contact

Auteur : Didier Flamm  
Date : Mai 2025
