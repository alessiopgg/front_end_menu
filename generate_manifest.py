from pathlib import Path
import json, re

IMAGES_DIR = Path("images")
OUT_FILE = Path("images.json")
EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}

def natural_key(name: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", name)]

def caption_from_filename(stem: str) -> str:
    return stem.replace("_"," ").replace("-"," ").strip().title()

def main():
    IMAGES_DIR.mkdir(exist_ok=True)
    files = [p for p in IMAGES_DIR.iterdir() if p.suffix.lower() in EXTS and p.is_file()]
    files.sort(key=lambda p: natural_key(p.name))
    items = [{"src": f"images/{p.name}", "caption": caption_from_filename(p.stem)} for p in files]
    OUT_FILE.write_text(json.dumps(items, ensure_ascii=False, indent=2))
    print(f"Creato {OUT_FILE} con {len(items)} immagini.")
if __name__ == "__main__":
    main()
