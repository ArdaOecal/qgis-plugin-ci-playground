import sys
from pathlib import Path

# Repo root (dummy_plugin.py'nin bulunduğu yer)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))