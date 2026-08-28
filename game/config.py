from pathlib import Path

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60

ROOT = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT / "assets"
RECORD_PATH = ROOT / "record"
SCORES = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}


def asset_path(filename: str) -> str:
    return str((ASSET_DIR / filename).resolve())
