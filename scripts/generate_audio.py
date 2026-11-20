"""Generate a small, explicitly approved test set of TOEIC Speaking audio."""
import asyncio
from pathlib import Path
import edge_tts

TEXT = (
    "In my opinion, working with a team is more effective. "
    "First, we can share different ideas. "
    "For example, my teammates helped me solve a difficult problem. "
    "As a result, we finished our project on time."
)
VOICE = "en-US-JennyNeural"

async def main():
    out = Path("audio")
    out.mkdir(exist_ok=True)
    for speed, rate in (("normal", "+0%"), ("slow", "-25%")):
        target = out / f"demo_teamwork_{speed}.mp3"
        await edge_tts.Communicate(TEXT, voice=VOICE, rate=rate).save(str(target))
        if target.stat().st_size < 2000:
            raise RuntimeError(f"Invalid or empty audio: {target}")
        print(f"Created {target} ({target.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
