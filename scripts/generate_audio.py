"""Generate original Day 1 TOEIC Speaking audio from checked-in lesson data."""
import asyncio
import json
from pathlib import Path
import edge_tts

VOICE = "en-US-JennyNeural"
RATES = (("normal", "+0%"), ("slow", "-25%"))

async def main():
    data = json.loads(Path("scripts/day1_payload.json").read_text(encoding="utf-8"))
    out = Path("audio")
    out.mkdir(exist_ok=True)
    for name, text in data["items"].items():
        for speed, rate in RATES:
            target = out / f'{data["id"]}_{name}_{speed}.mp3'
            await edge_tts.Communicate(text, voice=VOICE, rate=rate).save(str(target))
            if target.stat().st_size < 2000:
                raise RuntimeError(f"Empty audio: {target}")
            print(f"Created {target} ({target.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
