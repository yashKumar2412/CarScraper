# CarScraper

CarScraper is a platform designed to scrape car lease deals from various dealership websites, process and store the data in a structured format, and display the results through a simple web frontend.

## Features

- **Data Scraping**: Automated extraction of lease deals from multiple dealership websites using custom scrapers.
- **Data Processing**: Cleaning and organizing raw scraped data into structured CSV files.
- **Database Integration**: Persistent storage of processed data in a database for easy querying.
- **Frontend Display**: Simple and responsive web interface to display car deals and details.
- **Scalability**: Modular and extensible architecture for adding new dealerships and scaling.

## Project Structure

```plaintext
CarScraper/
├── cs-api/                   # Backend API implemented with Spring Boot
├── data/                     # Data storage
│   ├── csv/                  # Processed CSV files
│   ├── html/                 # HTML copies of scraped pages
│   ├── img/                  # Placeholder for scraped images
│   └── text/                 # Text-based deal data
├── frontend/                 # Web frontend files
├── scripts/                  # Python scripts for scraping and processing
│   ├── database/             # Database-related operations
│   ├── extractors/           # Data extractors
│   └── scrapers/             # Web scrapers
└── .gitignore                # Git ignore rules
```

## Versions Used
- Python: Version 3.12.6
- Java: JDK 17
- Maven: 3.4.1
- PostgreSQL
- ChromeDriver for Selenium

## Setup
Install the required Python libraries using:
```code
cd CarScraper
pip install -r scripts/requirements.txt
```

Create the car_deals table using the carscraper_db_create.sql script on your postgreSQL server. Update the database connection settings in both scripts/database/db_write.py and cs-api/src/main/resources/application.properties

Run the Python scripts
```code
python -m scripts.run_all
```

Run the backend Spring Boot server
```code
cd cs-api
mvn clean install
mvn spring-boot:run
```

Navigate to the frontend directory and open index.html in your browser.