#!/bin/bash

SOURCE_DIR="/home/liveuser/Desktop/at/ex4/documentos/"


BACKUP_DIR="/mnt/backup"


DATE=$(date +"%Y-%m-%d_%H-%M-%S")
DEST_DIR="$BACKUP_DIR/backup_$DATE"


LOG_FILE="$BACKUP_DIR/backup_log_$DATE.txt"


RSYNC_OPTIONS="-av --progress --delete"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Erro: O diretório de origem $SOURCE_DIR não existe!" | tee -a "$LOG_FILE"
    exit 1
fi


if [ ! -d "$BACKUP_DIR" ]; then
    echo "Criando diretório de backup $BACKUP_DIR..." | tee -a "$LOG_FILE"
    mkdir -p "$BACKUP_DIR"
fi



echo "Iniciando backup em $DATE..." | tee -a "$LOG_FILE"

rsync $RSYNC_OPTIONS "$SOURCE_DIR/" "$DEST_DIR" >> "$LOG_FILE" 2>&1


if [ $? -eq 0 ]; then
    echo "Backup concluído com sucesso em $DEST_DIR!" | tee -a "$LOG_FILE"
else
    echo "Erro durante o backup. Verifique o log em $LOG_FILE." | tee -a "$LOG_FILE"
    exit 1
fi

KEEP_BACKUPS=5
cd "$BACKUP_DIR" || exit
ls -d backup_* | sort -r | tail -n +$((KEEP_BACKUPS + 1)) | xargs -I {} rm -rf {}

echo "Limpeza concluída. Mantendo os últimos $KEEP_BACKUPS backups." | tee -a "$LOG_FILE"

exit 0