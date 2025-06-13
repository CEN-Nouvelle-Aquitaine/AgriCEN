#!/bin/bash

# -------------
# Configuration d'une tache cron pour nettoyer les sessions Flask
# -------------

# Chemin vers le dossier contenant les fichiers de session Flask
SESSION_DIR="/root/app_agricole/AgriCEN/flask_session"

# Fichier de log (au cas zou)
LOG_FILE="/root/app_agricole/AgriCEN/logs/flask_session_cleanup.log"

# Création du dossier de logs
mkdir -p "$(dirname "$LOG_FILE")"


# Vérifie que le dossier existe
if [ ! -d "$SESSION_DIR" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERREUR : Le dossier $SESSION_DIR n'existe pas." >> "$LOG_FILE"
    exit 1
fi


# Purge des fichiers de plus de 24h (1440 minutes)
echo "$(date '+%Y-%m-%d %H:%M:%S') - Début de la purge des sessions de plus de 24h." >> "$LOG_FILE"
find "$SESSION_DIR" -type f -mmin +1440 -print -delete >> "$LOG_FILE" 2>&1

# Fin de tâche
echo "$(date '+%Y-%m-%d %H:%M:%S') - Purge terminée." >> "$LOG_FILE"
