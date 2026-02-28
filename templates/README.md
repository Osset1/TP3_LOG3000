## Module : templates

### Raison d’être

Ce module est responsable de la présentation de l’interface utilisateur.  
Il permet de définir la structure du document affiché dans le navigateur
Il permet d’interagir avec les données fournies par le backend Flask.

### Fichiers principaux et responsabilités

- `index.html`  
  Définition de la structure de la page web en langage HTML avec le moteur de templates Jinja2.

### Dépendances et hypothèses

**Dépendances :**

- Framework Flask
- Jinja2
- Fichier de style `static/style.css`

**Hypothèses :**

- Le fichier CSS est présent dans le dossier `static`.
- Le navigateur de l’utilisateur supporte JavaScript.
- Les entrées utilisateur sont traitées côté serveur.
