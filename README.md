# Projet `WhiteApp`

Le package `WhiteApp` est un template BootStrap pour déploiement d'une chaîne CI/CD pour projet Flask (Python).

## Installation

### Environnement Python

Le projet utilise **python 3.8** dans un container Docker.

Le projet utilise également **pipenv**.
[Une ressource intéressante](https://moodle.insa-rouen.fr/pluginfile.php/75430/mod_resource/content/4/Python-PipPyenv.pdf).

L'ensemble des dépendances python sont listées dans le fichier `Pipfile`.
Celles-ci peuvent être installées à l'aide de pipenv avec `pipenv install [-d]`.

Pour télécharger l'ensemble des dépendances du projet afin de les porter ensuite 
sur une machine qui disposerait d'un accès limité à internet, il faut utiliser la commande
 `pipenv lock -r > requirements.txt` qui va transformer le `Pipfile` en un `requirements.txt`.

### Utilisation pour téléchargement des dépendances

A partir du fichier `requirements.txt`, il devient facile de télécharger les packages sous la forme 
de `wheels` pour les installer ensuite sur un environnement dépourvu de connexion internet.

Il faut utiliser la commande `pip download -d dossier -r path_to/requirements.txt` où `dossier` représente
le dossier dans lequel on veut stocker les `wheels` et `path_to` désigne le chemin vers le fichier `requirements.txt`
d'intérêt.

### Installation offline ultérieure

L'installation offline à partir des `wheels` préalablement téléchargées se fait avec la commande 
`pip install --no-index --find-links dossier` où `dossier` le dossier dans lequel on vient de
stocker les `wheels`.
