# Application Calculatrice Web – Devoir 3 LOG3000

**Équipe n° 30**

---

## Objectifs

Ce projet est une application web de calculatrice permettant d'effectuer des opérations arithmétiques simples, développée avec le framework Flask en Python.

L'objectif principal est de structurer, documenter et tester une base de code existante, initialement peu documentée et contenant des bogues.

---


## Prérequis

Avant de démarrer, assurez-vous d'avoir installé sur votre machine :

- **Git**
- **Python 3**
- **pip** (gestionnaire de paquets Python)

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Osset1/TP3_LOG3000
cd TP3_LOG3000
```

### 2. Créer et activer un environnement virtuel

**Création de l'environnement :**
```bash
python -m venv .venv
```

**Activation :**

- **MacOS et Linux :**
  ```bash
  source .venv/bin/activate
  ```

- **Windows :**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Installer les dépendances

```bash
pip install flask
```

### 4. Lancer l'application

```bash
python3 app.py
```

### 5. Accéder à l'application

Ouvrez votre navigateur et accédez à l'adresse suivante :
```
http://127.0.0.1:5000
```

---

## Exécution des tests

Depuis le répertoire racine du projet :

```bash
cd tests
python -m unittest discover
```

---

## Contribution

### Structure des branches

- **main** : branche stable contenant le code en production
- **Branches de fonctionnalités :** `documentation/nom-feature-documentée`
- **Branches de correctifs :** `bugfix/nom-bug`

### Issues

- Toute anomalie ou amélioration doit être documentée via une **issue GitHub**
- Chaque issue doit décrire clairement le problème, fournir les étapes de reproduction ou les cas de test en échec, et être assignée à un membre de l'équipe

### Pull Requests

- Chaque branche de modification doit posséder une **pull request**
- Chaque pull request doit être liée à une issue existante
- Une **revue de code** doit être effectuée avant la fusion d'une branche