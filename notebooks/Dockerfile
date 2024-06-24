# Utilisation d'une image Python 3.8 slim
FROM python:3.8-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /notebooks

# Copie des fichiers de dépendances et installation
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copie des notebooks et des données locaux vers le conteneur
COPY . .

# Exposer le port sur lequel Jupyter Lab va écouter
EXPOSE 8888

# Commande pour démarrer Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
