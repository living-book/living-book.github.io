#!/bin/bash
# Stage 4: synthesize audio overviews. Idempotent — skips existing mp3s.
set -u
SCRIPTS=${1:-/home/sanjayg4/living-books/scripts/audio_scripts}
OUT=${2:-/home/sanjayg4/living-books/docs/books/laws-of-human-nature/audio}
TMP=$(mktemp -d)
cd /home/sanjayg4/chatterbox
for f in "$SCRIPTS"/*.txt; do
  base=$(basename "$f" .txt)
  [ -f "$OUT/$base.mp3" ] && { echo "skip $base"; continue; }
  ./voice --text "$f" --out "$TMP/$base.wav" >/dev/null 2>&1
  if [ -f "$TMP/$base.wav" ]; then
    ffmpeg -y -loglevel error -i "$TMP/$base.wav" -codec:a libmp3lame -b:a 96k "$OUT/$base.mp3"
    echo "ok   $base ($(du -h "$OUT/$base.mp3" | cut -f1))"
  else
    echo "FAIL $base"
  fi
done
rm -rf "$TMP"
echo done
