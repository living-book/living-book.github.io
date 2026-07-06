#!/bin/bash
# Stage 4: synthesize audio overviews. Idempotent (skips existing) unless FORCE=1.
# Voice config via VOICE_ARGS (default: locked warm/scholarly — chosen 2026-07-06).
# Usage: [FORCE=1] [VOICE_ARGS="..."] gen_audio.sh <scripts_dir> <out_dir>
set -u
SCRIPTS=${1:-/home/sanjayg4/living-books/scripts/audio_scripts}
OUT=${2:-/home/sanjayg4/living-books/docs/books/laws-of-human-nature/audio}
VOICE_ARGS=${VOICE_ARGS:-"--style warm --exaggeration 0.35 --cfg-weight 0.5"}
FORCE=${FORCE:-0}
# resolve to absolute — the cd below breaks any relative path (bit us 2026-07-06)
SCRIPTS=$(realpath "$SCRIPTS")
mkdir -p "$OUT"; OUT=$(realpath "$OUT")
TMP=$(mktemp -d)
cd /home/sanjayg4/chatterbox
for f in "$SCRIPTS"/*.txt; do
  base=$(basename "$f" .txt)
  if [ "$FORCE" != "1" ] && [ -f "$OUT/$base.mp3" ]; then echo "skip $base"; continue; fi
  ./voice $VOICE_ARGS --text "$f" --out "$TMP/$base.wav" >/dev/null 2>&1
  if [ -f "$TMP/$base.wav" ]; then
    ffmpeg -y -loglevel error -i "$TMP/$base.wav" -codec:a libmp3lame -b:a 96k "$OUT/$base.mp3"
    echo "ok   $base ($(du -h "$OUT/$base.mp3" | cut -f1))"
  else
    echo "FAIL $base"
  fi
done
rm -rf "$TMP"
echo done
