"""Offline text-to-speech with Kokoro.

Usage: python tools/tts.py "text or path/to/script.txt" out.wav [--voice am_michael] [--speed 1.0]
"""
import argparse
import os
import pathlib

import soundfile as sf
from kokoro_onnx import Kokoro

MODEL_DIR = pathlib.Path(os.environ.get("KOKORO_DIR", pathlib.Path.home() / "tts-models"))

p = argparse.ArgumentParser()
p.add_argument("text")
p.add_argument("out")
p.add_argument("--voice", default="am_michael")
p.add_argument("--speed", type=float, default=1.0)
p.add_argument("--lang", default="en-us")
a = p.parse_args()

text = pathlib.Path(a.text).read_text() if os.path.isfile(a.text) else a.text
kokoro = Kokoro(str(MODEL_DIR / "kokoro-v1.0.onnx"), str(MODEL_DIR / "voices-v1.0.bin"))
samples, rate = kokoro.create(text, voice=a.voice, speed=a.speed, lang=a.lang)
sf.write(a.out, samples, rate)
print(f"wrote {a.out} ({len(samples) / rate:.1f}s)")
