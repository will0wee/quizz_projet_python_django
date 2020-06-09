# quizz_projet_python_django

Notre projet a pour but de créer un quizz pour une classe afin de l'évaluer sur un sujet defini.

L'application comporte deux type d'utilisateurs, qui sont les Professeurs et les Eleves.
  
  • Les professeurs pourront créer des quizz, les modifier, inspecter les notes des élèves et gerer les classes.
    Ils peuvent ajouter des élèves aux classes qui leur correspondent afin de leur permettre de participer aux quizz.
  
  
  • Les élèves peuvent accéder à leur quizz proposés sur leur homepage apres connexion. Ils peuvent acceder à leur dernieres notes des       quizz précédents.
  
  Tout utilisateur peut acceder à son profil personnel afin de modifier ses informations de communication.
  
  Nous avons choisi pour template, un template existant nommé INSPINIA https://github.com/whitecolor/inspinia-admin .
  
  # Details du projet
  >>User
    • Une page de login est faite afin de se connecter au site. Seul l'administrateur peut créer un compte pour qu'un utilisateur puisse se connecter.
  
    • Apres la page de connexion de l'utilisateur, ce dernier atteindra la page Home. Cette page permet principalement aux étudiants d'accéder à leurs nouveau quizz organisé . Les professeurs, eux, pourront voir les quizz créés.
    
    •  Les utilisateurs peuvent accéder à leur profil personnel et modifier leurs informations personnelles via le bouton comportant leur nom en haut à gauche de la page.
    
    
  >>Quizz
  
  •   La page add_quizz permet au professeur d'ajouter un quizz pour les etudiants.
  
  •   Les élèves peuvent voir les quizz à faire sur la page doQuizz et le professeurs pour y voir la liste des quizz faite.
  
  •   Les étudiants font leurs quizz grâce à la page homeQuizzEleve, où il y trouveront une interface de remplission de quizz.
  
  •   Les professeurs peuvent voir le nombre de quizz en attente demandés au élèves et le nombre de quizz terminé (ceux au moins commencés par les élèves).
  
  •   La page listeInstanceQuizz va permettre de récupérer les noms, dates et notes des personnes ayant répondu au quizz créé.
  
  •   La page quizzDetail permet de voir les réponses envoyés par les élèves à un quizz créé.
