#!/usr/bin/env bash
# Install the YouTube downloader (yt-dlp) and offline TTS (Kokoro) used for shorts.
set -euo pipefail

pip install -q -U yt-dlp kokoro-onnx soundfile

MODEL_DIR="${KOKORO_DIR:-$HOME/tts-models}"
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
mkdir -p "$MODEL_DIR"
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$MODEL_DIR/$f" ] || curl -sSL -o "$MODEL_DIR/$f" "$BASE/$f"
done

echo "yt-dlp $(yt-dlp --version); Kokoro models in $MODEL_DIR"
