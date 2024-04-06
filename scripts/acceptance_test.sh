#!/bin/bash
set -euxo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
"$DIR"/deploy_locally.sh

BATCH_FILE="/tmp/batch-file.txt"
DOWNLOAD_FOLDER="/tmp/download"
ALREADY_DOWNLOADED="/tmp/already-downloaded.txt"

mkdir -p "$DOWNLOAD_FOLDER" && rm -f "$DOWNLOAD_FOLDER"/*
echo "" > "$ALREADY_DOWNLOADED"
echo "https://www.youtube.com/watch?v=qrO4YZeyl0I" > /tmp/batch-file.txt

get_mp3_from_url -b "$BATCH_FILE" -d "$DOWNLOAD_FOLDER" -a "$ALREADY_DOWNLOADED"

if ! find "$DOWNLOAD_FOLDER" -maxdepth 1 -type f -name "*.mp3" -print -quit | grep -q .; then
    echo "ERROR: No .mp3 file found in $DOWNLOAD_FOLDER"
    exit 1
fi

if find "$DOWNLOAD_FOLDER" -maxdepth 1 -type f -name "*.webp" -print -quit | grep -q .; then
    echo "ERROR: .webp file found in $DOWNLOAD_FOLDER"
    exit 1
fi
