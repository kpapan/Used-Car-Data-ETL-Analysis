# CARS_ETL_PROJECT

This project processes and analyzes data from used car advertisements. It includes data cleaning, transformation, database integration with PostgreSQL, and analysis using SQL and Python.

## Workflow

- Load and clean raw dataset (CSV format)
- Apply transformations and create new features
- Store cleaned data in PostgreSQL using SQLAlchemy
- Analyze and visualize data with SQL queries and Python
- Log each ETL step

## Technologies Used

- Python (pandas, numpy, matplotlib, seaborn)
- PostgreSQL
- SQLAlchemy
- dotenv
- Jupyter Notebooks

## Folder Structure

- `cars_data_analysis/`: Notebook for SQL queries and visualizations  
- `data/`: Raw and cleaned datasets  
- `loading_to_db/`: Scripts and env config to connect to DB and load data  
- `process.py`: Main ETL script  
- `transformations.py`: Preprocessing functions  
- `requirements.txt`: Required libraries  
- `log.txt`: ETL log  
- `.env`: Contains DB credentials (excluded from Git)

## Getting Started

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file in both cars_data_analysis/ and loading_to_db/ folders with the following content:
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database

# 3. Run the ETL script
python process.py

## Dataset

The dataset used in this project can be found on Kaggle:  
[Used Cars for Sale in Poland – Kaggle Dataset](https://www.kaggle.com/datasets/bartoszpieniak/poland-cars-for-sale-dataset)

