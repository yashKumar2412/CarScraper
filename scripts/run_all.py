import subprocess

# List of commands to run
commands = [
    "python -m scripts.scrapers.audi_scraper",
    "python -m scripts.scrapers.volvo_scraper",
    "python -m scripts.scrapers.honda_scraper",
    "python -m scripts.extractors.audi_extractor",
    "python -m scripts.extractors.volvo_extractor",
    "python -m scripts.extractors.honda_extractor",
    "python -m scripts.database.csv_merger",
    "python -m scripts.database.db_write"
]

# Execute each command in order
for command in commands:
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running: {command}")
        print(f"Error Output:\n{e.stderr}")
        break