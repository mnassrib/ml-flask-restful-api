# Utilisation d'une image Python slim
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier seulement le fichier des dépendances d'abord
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier les fichiers et répertoires locaux vers le conteneur
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application flask
CMD ["python", "app.py"]