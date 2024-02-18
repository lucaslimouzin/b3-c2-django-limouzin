Projet Django gestionnaire de Mot de passe
Afin de pouvoir lancer correctement le projet : 
- Vérifier d'avoir bien installé Python + Django sur sa machine.
- cd passwordManager
- pip install -r
- python manage.py migrate
- python manage.py runserver

  Si toutes les etapes précédentes sont validées vous devrez pouvoir accèder à la page du site
  /home la page d'accueil
  /admin la page d'admin

  pour gérer la page d'admin des logs de basent sont présent :
  id: admin
  password: admin

  Fonctionnalités présentes :
  - Inscription et connexion d'un utilisateur
  - Ajout d'un site avec son nom + url + id + mdp
  - Visualisation du site et de ses informations
  - Modification d'un site
  - Supression d'un site
  - Exportation via csv
  - importation via csv
  - Dark Mode
