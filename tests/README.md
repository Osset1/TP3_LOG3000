## Module : tests

### Exécution des tests

Depuis le répertoire racine du projet :

```bash
cd tests
python -m unittest discover
```

### Raison d’être

Ce module est responsable de la validation du comportement de l’application.
Il permet de vérifier le bon fonctionnement des opérations de la calculatrice web.
Il permet de détecter les régressions lors des modifications du code.

### Fichiers principaux et responsabilités

- `tests_operators.py`  
  Tests unitaires pour les opérations mathématiques : addition, soustraction, multiplication et division.

### Dépendances et hypothèses

**Dépendances :**

- unittest
- sys
- Module operators

**Hypothèses :**

- Les fonctions opérationnelles prennent en entrée des entiers positifs et négatifs.
- Les fonctions retournent des résultats numériques valides pour les opérations supportées.
