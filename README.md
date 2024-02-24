# Django  simple Authentication System
C'est un systéme d'autentification simple, permettant de gérer les utilisateurs et les groupes et également l'attributions des permissions.

Ce systéme ne gére pas, lors de la création du compte, l'envoit d'un email à l'utilisateur d'activer son compte. Dés qu'il crée son compte, celui-ci est activé et redirigé vers sa page login où il pourra se logger à son profile.

Les utilisateurs sont identifiés avec leur Username

En cas de Réstauration de mot de passe, un email et envoyer à l'utiliseur lui rédireger vers la passe de restauration de mot de passse.

## Admin
1. Manager les utiliseurs 
2. Manager les Groupes
3. Manager les permissions

## L'utilisateur simple
1. Crée un compte 
2. Se Connecter 
3. Peut se Déconnecter
3. Peut Change de Mot de Passe
4. Peut Restorer un Mot de passe

## Comment Installer et Demarrer ce projet?

### Pre-requis:
1. Installer Git
[ https://git-scm.com/ ]

2. Installer Python Derniére Version
[ https://www.python.org/downloads/ ]

### Installation
**1. Créer un dossier dans lequel vous souhaitez enregistrer le projet**

**2. Créer un environnement virtuel et activez**
Ouvre ce dossier dans ton éditeur de Code
Allez-y dans votre terminal gitbash

Installer l'Environnement Virtuel
```
pip install virtualenv
```

Création de l'Environnement virtuel:

Sur Window
```
python -m venv .env
```
Sur Mac
```
python3 -m venv .env
```

Activation de l'Environnement Virtuel

Sur Windows
```
source .env/scripts/activate
```

Sur Mac
```
source .env/bin/activate
```

**3. Cloner le projet**
```
git clone https://github.com/harouna227/authentification-system.git
```
Une fois cloné, rentrer dans le dossier src
```
cd src
```

**4. Installer les exigences dépuis 'requirements.txt'**
```
pip install -r requirements.txt
```

**5. Congiguration d'envoi d'email par SMTP lors de restauration de mot de passe**

Vous pouvez configurer ça aussi, aprés le demarrage du Serveur

- allez-y dans le fichier settings.py se trouvant dans le dossier core
- A la variable **EMAIL_HOST_USER** affecter votre mail configuré sur votre compte google pour test. Mettez un email fonctionnel.
- A la variable **EMAIL_HOST_PASSWORD** affecter le mot de passe générer au niveau de votre compte google

Vous pouvez aussi faire une configuration locale d'envoi d'email avec MAILHOC.

**6. Idenfiant de Connexion**

Créer un Super utiliseur (Admin)

Sur Windows:
```
python manage.py createsuperuser
```

Sur MAC:
```
python3 manage.py createsuperuser
```
Ensuite ajouter Usename, Email, et mot de passe

### Demarrage
**1.  Maintenant demarrer le Serveur**

Sur Windows:
```
python manage.py runserver
```

Sur Mac:
```
python3 manage.py runserver
```

**2. Copier et Caller l'Addresse locale sur laquelle le serveur est demarragée dans votre navigateur**

```
http://127.0.0.1:8000/
```

**3. Connexion à la page Admin avec ses indentifiants**
```
http://127.0.0.1:8000/admin/
```