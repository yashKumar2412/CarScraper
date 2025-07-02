from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Data directories
HTML_DIR = DATA_DIR / "html"
TEXT_DIR = DATA_DIR / "text"
CSV_DIR = DATA_DIR / "csv"
IMG_DIR = DATA_DIR / "img"

# Make sure directories exist
HTML_DIR.mkdir(parents=True, exist_ok=True)
TEXT_DIR.mkdir(parents=True, exist_ok=True)
CSV_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

# File paths for Audi
AUDI_HTML = HTML_DIR / "audi_deals.html"
AUDI_TEXT = TEXT_DIR / "audi_deals.txt"
AUDI_IMG = IMG_DIR / "audi_deals.txt"
AUDI_CSV = CSV_DIR / "audi_deals.csv"

# File paths for Volvo
VOLVO_HTML = HTML_DIR / "volvo_deals.html"
VOLVO_TEXT = TEXT_DIR / "volvo_deals.txt"
VOLVO_IMG = IMG_DIR / "volvo_deals.txt"
VOLVO_CSV = CSV_DIR / "volvo_deals.csv"

# File paths for Honda
HONDA_HTML = HTML_DIR / "honda_deals.html"
HONDA_TEXT = TEXT_DIR / "honda_deals.txt"
HONDA_IMG = IMG_DIR / "honda_deals.txt"
HONDA_CSV = CSV_DIR / "honda_deals.csv"

# File paths for combined deals
COMBINED_CSV = CSV_DIR / "combined_deals.csv"