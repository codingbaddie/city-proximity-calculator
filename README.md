# City Proximity Calculator

This project calculates the three nearest cities for each city in a given dataset based on geographical coordinates.

## Description

The City Proximity Calculator is a Python script that reads a CSV file containing city information (including latitude and longitude), calculates the distances between cities, and identifies the three nearest neighboring cities for each city in the dataset. The results are then output to a new CSV file.

## Features

- Reads city data from a CSV file
- Calculates distances between cities using the Haversine formula
- Identifies the three nearest cities for each city
- Outputs results in a CSV format for easy viewing and analysis

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/city-proximity-calculator.git
   ```
2. Navigate to the project directory:
   ```
   cd city-proximity-calculator
   ```
3. Install the required Python packages:
   ```
   pip install pandas geopy tqdm
   ```

## Usage

1. Place your input CSV file named `List of ID Cities - Sheet1.csv` in the project directory.
2. Run the script:
   ```
   python city_proximity_calculator.py
   ```
3. After execution, find the results in `nearest_cities_results.csv` in the same directory.

## Input File Format

The input CSV file should have the following columns:
- l2_province
- l3_city_id
- l3_city
- longitude
- latitude

## Output File Format

The output CSV file will contain the following columns:
- Province
- city ID
- city
- nearby 1
- nearby 2
- nearby 3

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please contact [Your Name] at [rachel880508@gmail.com].