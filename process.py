import os
import logging
from transformations import (
    load_data,
    filter_used_cars,
    select_features,
    remove_duplicates,
    convert_currency,
    clean_price_column,
    impute_missing_values,
    handle_outliers_multiple_columns,
    get_numerical_columns
)

# ----------------------------
# Logging Setup
# ----------------------------
log_file = "log.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ----------------------------
# Main ETL process
# ----------------------------
def process(data_path, output_path):
    logger.info("ETL process started.")

    # 1. Load raw data
    df, _ = load_data(data_path)

    # 2. Filter used cars
    df = filter_used_cars(df)

    # 3. Select only needed columns
    df = select_features(df)

    # 4. Handle duplicates & sort
    df = remove_duplicates(df)

    # 5. Convert currencies
    df = convert_currency(df)

    # 6. Clean Price column
    df = clean_price_column(df)

    # 7. Handle missing values
    df = impute_missing_values(df)

    # 8. Handle outliers
    numerical_cols = get_numerical_columns(df)
    df = handle_outliers_multiple_columns(df, numerical_cols)

    # 9. Save to CSV
    df.to_csv(output_path, index=False)
    logger.info(f" Clean dataset saved to: {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    input_file = os.path.join(data_dir, "Car_sale_ads.csv.zip")
    output_file = os.path.join(data_dir, "Car_sale_ads_clean.csv")

    process(input_file, output_file)
