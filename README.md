# API pour une application de pédiction avec Flask-RESTful et Docker

Ce projet utilise Flask-RESTful pour simplifier la création de l'API REST, en suivant les pratiques courantes pour la construction de services RESTful. La documentation et la structure du projet sont conçues pour être claires et faciles à comprendre.

## Objectif

L'objectif de ce projet est de créer une API permettant de faire des prédictions en utilisant un modèle de Machine Learning. Cette API est construite avec Flask et Flask-RESTful, et utilise Docker pour une gestion facile des dépendances et du déploiement. Un service JupyterLab est également inclus pour l'entraînement interactif du modèle.

## Structure du projet

Le projet est structuré comme suit :

```
ml-flask-restful-api/
├── api/
│   ├── app.py
│   ├── Dockerfile
│   ├── model.pkl
│   └── requirements.txt
├── jupyter/
│   ├── train_model_4_features.ipynb
│   ├── train_model_5_features.ipynb
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

### api/

Contient le code de l'API Flask.

- **app.py** : Code source de l'API Flask.
- **model.pkl** : Un modèle pour la prédiction.
- **Dockerfile** : Instructions pour construire l'image Docker de l'API.
- **requirements.txt** : Dépendances Python pour l'API Flask.

### jupyter/

Contient le notebook Jupyter pour l'entraînement du modèle.

- **train_model_4_features.ipynb** : Un premier Notebook Jupyter pour entraîner et sauvegarder le modèle.
- **train_model_5_features.ipynb** : Un deuxième Notebook Jupyter pour entraîner et sauvegarder le modèle.
- **Dockerfile** : Instructions pour construire l'image Docker de JupyterLab.
- **requirements.txt** : Dépendances Python pour JupyterLab.

### docker-compose.yml

Fichier de configuration Docker Compose pour orchestrer les conteneurs API et JupyterLab.

## Volumes et relations

Les volumes permettent de partager des fichiers entre les conteneurs et l'hôte, facilitant ainsi l'accès aux modèles sauvegardés.

- **api** service :
  - `./api:/app` : Monte le répertoire `./api` de l'hôte dans `/app` dans le conteneur API.
  - Permet à l'API Flask d'accéder au modèle sauvegardé.

- **jupyter** service :
  - `./jupyter:/home/jovyan` : Monte le répertoire `./jupyter` de l'hôte dans `/home/jovyan` dans le conteneur JupyterLab.
  - `./api:/app` : Monte le répertoire `./api` de l'hôte dans `/app` dans le conteneur JupyterLab.
  - Permet à JupyterLab de sauvegarder le modèle dans un répertoire partagé accessible par l'API.

## Cloner le dépôt

```bash
git clone https://github.com/mnassrib/ml-flask-restful-api.git
cd ml-flask-restful-api
```

## Commandes

### Construction, lancement et arrêt des conteneurs

- Pour construire et lancer les conteneurs, utilisez Docker Compose :

```sh
docker-compose up --build
```

- Pour arrêter et supprimer les conteneurs créés par `docker-compose up`, utilisez la commande suivante :
  
```bash
docker-compose down
```

### Accéder à JupyterLab

Ouvrez votre navigateur et accédez à `http://localhost:8888` pour utiliser JupyterLab. Utilisez un des notebooks `train_model_?_features.ipynb` pour entraîner et sauvegarder un modèle.

### Tester l'API Flask

L'API Flask est accessible sur `http://localhost:5000/predict`. Envoyez une requête POST avec les caractéristiques à prédire. Par exemple, utilisez `curl` :

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Utilisation de l'API

L'API sera accessible à `http://localhost:5000`.

#### Endpoint `/predict`

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

###### Utilisation de l'extension REST Client pour Chrome

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

###### Utilisation de l'extension RESTer pour Firefox

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

###### Conclusion

En suivant ces étapes avec l'extension REST Client pour Chrome ou RESTer pour Firefox, vous pouvez facilement tester des requêtes POST directement depuis le navigateur. Assurez-vous que votre application Flask est en cours d'exécution sur `http://127.0.0.1:5000` et que votre endpoint `/predict` est configuré pour accepter et traiter les requêtes POST avec des données JSON. Cela vous permettra de vérifier le bon fonctionnement de votre API Flask avec différentes entrées de données.

---

#### Endpoint `/health`

- **URL:** `/health`
- **Méthode:** `GET`
- **Description:** Vérifie l'état de l'API.
- **Exemple de réponse:**
  ```json
  {
      "status": "OK"
  }
  ```

## Entraînement d'un modèle

Exécutez un des notebooks `train_model_?_features.ipynb` pour entraîner le modèle et le sauvegarder dans `/app/model.pkl` qui sera utilisé par l'API Flask. Cette dernièrre chargera le modèle depuis `/app/model.pkl`, accessible via `./api/model.pkl` sur l'hôte.

L'une des grandes avantages d'utiliser Docker avec des volumes montés est que les modifications apportées aux fichiers dans les volumes montés sont immédiatement disponibles dans le conteneur sans avoir besoin de redémarrer le conteneur. Voici comment cela fonctionne :

### Flux de travail pour la mise à jour du modèle

1. **Entraînement et sauvegarde du modèle avec JupyterLab** :
   - Vous utilisez JupyterLab pour réentraîner le modèle et le sauvegarder dans le répertoire `/app`, qui correspond à `./api` sur l'hôte.
   - Exemple : Vous exécutez un des notebooks `train_model_?_features.ipynb` qui réentraîne le modèle et sauvegarde le nouveau modèle dans `/app/model.pkl`.

2. **Accès immédiat par l'API Flask** :
   - L'API Flask est déjà configurée pour charger le modèle depuis `/app/model.pkl` lors de la réception d'une requête.
   - Si le fichier `model.pkl` est mis à jour, le conteneur API verra automatiquement la nouvelle version du fichier.

### Conclusion

Avec les volumes montés de Docker, les modifications apportées au modèle sauvegardé par JupyterLab seront automatiquement disponibles pour le conteneur API. Pour refléter les changements du modèle sans redémarrer l'API Flask, vous pouvez recharger le modèle dynamiquement soit à chaque requête, soit via un endpoint spécifique pour le rechargement. Cela permet une flexibilité maximale pour mettre à jour et utiliser votre modèle de machine learning en production.

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une issue ou une pull request.
