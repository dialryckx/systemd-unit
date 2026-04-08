#!/bin/bash

SERVICE_NAME="httpserver.service"
SOURCE_PATH="./$SERVICE_NAME"
DEST_PATH="/etc/systemd/system/"

# 1. Проверка наличия исходного файла
if [ ! -f "$SOURCE_PATH" ]; then
    echo "Error: File $SOURCE_NAME not found in $SOURCE_PATH"
    exit 1
fi

echo "Installing $SERVICE_NAME..."

sudo cp "$SOURCE_PATH" "$DEST_PATH"

sudo chmod 644 "$DEST_PATH$SERVICE_NAME"

echo "Reload configuration systemd..."
sudo systemctl daemon-reload

echo "Enabling autostart..."
sudo systemctl enable "$SERVICE_NAME"

# 6. Запуск службы прямо сейчас
echo "Starting service..."
sudo systemctl start "$SERVICE_NAME"

echo "Done! Service status:"
sudo systemctl status "$SERVICE_NAME" --no-pager
