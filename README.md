# API pour un Modèle de Machine Learning avec Flask-RESTful et Docker

Ce projet utilise Flask-RESTful pour simplifier la création de l'API REST, en suivant les pratiques courantes pour la construction de services RESTful. La documentation et la structure du projet sont conçues pour être claires et faciles à comprendre.

## Description

Cette API permet de faire des prédictions en utilisant un modèle de Machine Learning. Elle est construite avec Flask et Flask-RESTful, et utilise Docker pour une gestion facile des dépendances et du déploiement.

## Structure du projet

```
ml-flask-restful-api/
├── app/
│   ├── api.py
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── model/
│   └── model.pkl
├── notebooks/
│   ├── train_model.ipynb
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation et exécution

### Prérequis

- Docker
- Docker compose

---
#### docker-compose.yml

Ce fichier `docker-compose.yml` est une configuration pour Docker Compose, un outil qui permet de définir et de gérer des applications multi-conteneurs Docker. Voici une explication détaillée du contenu de ce fichier :

##### Service `api` :

```yaml
services:
  api:
    build: ./app
    container_name: flask-restful-api
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
      - ./model:/model
```

- **build**: Indique le chemin vers le répertoire contenant le `Dockerfile` pour construire l'image Docker du service `api`. Dans ce cas, il se trouve dans le répertoire `./app`.
  
- **container_name**: Spécifie le nom du conteneur Docker qui sera créé pour le service `api`. Ici, il est nommé `flask-restful-api`.
  
- **ports**: Définit le mapping des ports entre le conteneur et l'hôte. Dans ce cas, le port `5000` du conteneur est exposé sur le port `5000` de l'hôte (votre machine locale).
  
- **volumes**: Montre les volumes Docker utilisés pour partager des données entre le conteneur et l'hôte. Les chemins spécifiés (`./app` et `./model`) montent les répertoires locaux dans les chemins correspondants à l'intérieur du conteneur (`/app` et `/model`).

##### Service `jupyter` :

```yaml
  jupyter:
    build: ./notebooks
    container_name: jupyter
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/notebooks
      - ./model:/model
    environment:
      - JUPYTER_ENABLE_LAB=yes
```

- **build**: Spécifie le chemin vers le répertoire contenant le `Dockerfile` pour construire l'image Docker du service `jupyter`. Dans ce cas, il se trouve dans le répertoire `./notebooks`.
  
- **container_name**: Nomme le conteneur Docker créé pour le service `jupyter` en tant que `jupyter`.
  
- **ports**: Mappe le port `8888` du conteneur sur le port `8888` de l'hôte (votre machine locale), permettant l'accès à Jupyter Lab depuis votre navigateur.
  
- **volumes**: Montre les volumes Docker utilisés pour partager des données entre le conteneur et l'hôte. Les chemins spécifiés (`./notebooks` et `./model`) montent les répertoires locaux dans les chemins correspondants à l'intérieur du conteneur (`/notebooks` et `/model`).
  
- **environment**: Définit les variables d'environnement spécifiques au conteneur. Ici, `JUPYTER_ENABLE_LAB=yes` indique que Jupyter Lab doit être activé lorsque le conteneur démarre.

#### Utilisation de docker-compose.yml

- Pour démarrer les services définis dans ce fichier `docker-compose.yml`, vous pouvez exécuter la commande suivante à partir du répertoire où se trouve ce fichier :
  
  ```bash
  docker-compose up
  ```
  
  Cette commande construira les images Docker spécifiées dans les `Dockerfile`, créera et démarrera les conteneurs correspondants (`api` et `jupyter`), en suivant les configurations définies.

- Pour arrêter et supprimer les conteneurs créés par `docker-compose up`, utilisez la commande suivante :
  
  ```bash
  docker-compose down
  ```
---

### Étapes

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/mnassrib/ml-flask-restful-api.git
    cd ml-flask-restful-api
    ```

2. Construire et démarrer les conteneurs Docker :
    ```bash
    docker-compose up --build
    ```

3. L'API sera accessible à `http://localhost:5000`.

## Utilisation de l'API

### Endpoint `/predict`

- **URL:** `/predict`
- **Méthode:** `POST`
- **Paramètres:**
  - `features`: liste des caractéristiques pour la prédiction.
- **Exemple de requête:**
  ```json
  {
      "features": [1, ...]
  }
  ```
- **Exemple de réponse:**
  ```json
  {
      "prediction": [0]
  }
  ```

---
#### Tester une requête POST directement depuis le navigateur

Pour tester une requête POST directement depuis le navigateur en utilisant une extension comme "REST Client" pour Chrome ou "RESTer" pour Firefox, suivez les étapes détaillées ci-dessous :

##### Utilisation de l'extension REST Client pour Chrome

1. **Installation de l'extension REST Client** :
   - Ouvrez le navigateur Chrome.
   - Accédez à la page d'extension de Chrome Web Store pour REST Client.
   - Cliquez sur le bouton "Ajouter à Chrome" pour installer l'extension.

2. **Ouverture de l'extension** :
   - Une fois installée, cliquez sur l'icône de l'extension REST Client dans la barre d'outils de Chrome pour l'ouvrir.

3. **Configurer la requête POST** :
   - Dans REST Client, cliquez sur le signe plus (+) pour créer une nouvelle requête.
   - Sélectionnez POST comme méthode de requête.

4. **Ajouter l'URL et les détails de la requête** :
   - Dans le champ URL, saisissez `http://127.0.0.1:5000/predict`.
   - Assurez-vous que le type de contenu est défini sur `application/json`. Vous pouvez ajouter cet en-tête dans la section des en-têtes de la requête.
   - Dans la section du corps de la requête, ajoutez les données JSON que vous souhaitez envoyer à votre endpoint Flask. Par exemple :
     ```json
     {
       "features": [1, ...]
     }
     ```

5. **Envoyer la requête** :
   - Une fois que vous avez configuré tous les détails nécessaires (URL, méthode POST, en-têtes, corps de la requête), cliquez sur le bouton "Send" pour envoyer la requête à votre application Flask.

##### Utilisation de l'extension RESTer pour Firefox

1. **Installation de l'extension RESTer** :
   - Ouvrez le navigateur Firefox.
   - Accédez à la page d'extension de Firefox Add-ons pour RESTer.
   - Cliquez sur le bouton "Add to Firefox" pour installer l'extension.

2. **Ouverture de l'extension** :
   - Une fois installée, cliquez sur l'icône de l'extension RESTer dans la barre d'outils de Firefox pour l'ouvrir.

3. **Configurer la requête POST** :
   - Dans RESTer, cliquez sur le bouton "New Request" pour créer une nouvelle requête.
   - Sélectionnez POST comme méthode de requête.

4. **Ajouter l'URL et les détails de la requête** :
   - Dans le champ URL, saisissez `http://127.0.0.1:5000/predict`.
   - Ajoutez l'en-tête `Content-Type` avec la valeur `application/json`. Vous pouvez ajouter cet en-tête dans la section des en-têtes de la requête.
   - Dans la section du corps de la requête, ajoutez les données JSON que vous souhaitez envoyer à votre endpoint Flask. Par exemple :
     ```json
     {
       "features": [1, ...]
     }
     ```

5. **Envoyer la requête** :
   - Une fois que vous avez configuré tous les détails nécessaires (URL, méthode POST, en-têtes, corps de la requête), cliquez sur le bouton "Send" pour envoyer la requête à votre application Flask.

##### Conclusion

En suivant ces étapes avec l'extension REST Client pour Chrome ou RESTer pour Firefox, vous pouvez facilement tester des requêtes POST directement depuis votre navigateur. Assurez-vous que votre application Flask est en cours d'exécution sur `http://127.0.0.1:5000` et que votre endpoint `/predict` est configuré pour accepter et traiter les requêtes POST avec des données JSON. Cela vous permettra de vérifier le bon fonctionnement de votre API Flask avec différentes entrées de données.

---

### Endpoint `/health`

- **URL:** `/health`
- **Méthode:** `GET`
- **Description:** Vérifie l'état de l'API.
- **Exemple de réponse:**
  ```json
  {
      "status": "OK"
  }
  ```

## Entraînement du modèle

Pour réentraîner le modèle ou entraîner un nouveau modèle sur un nouveau jeu de données, exécutez le script `notebooks/train_model.ipynb`. Cela générera un fichier `model.pkl` qui sera utilisé par l'API pour les prédictions.

Redémarrer votre application Flask : Après avoir mis à jour le modèle sauvegardé, redémarrez votre application Flask. Cela peut être fait manuellement en arrêtant le conteneur Docker Flask actuel (docker-compose down ou docker stop <container_id>) et en le relançant (docker-compose up --build ou docker-compose up -d si vous utilisez Docker Compose).

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une issue ou une pull request.
