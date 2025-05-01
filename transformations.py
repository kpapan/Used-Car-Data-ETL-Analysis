import pandas as pd
import logging

logger = logging.getLogger(__name__)

# ----------------------------
# 1. Load & Backup
# ----------------------------
def load_data(path):
    logger.info("Loading dataset...")
    df = pd.read_csv(path)
    df_backup = df.copy()
    logger.info(f"Dataset loaded with {len(df)} rows.")
    return df, df_backup

# ----------------------------
# 2. Keep only used cars
# ----------------------------
def filter_used_cars(df):
    logger.info("Filtering used cars...")
    filtered_df = df[df['Condition'] == 'Used']
    logger.info(f"{len(filtered_df)} used cars remaining.")
    return filtered_df

# ----------------------------
# 3. Select Features
# ----------------------------
def select_features(df):
    logger.info("Selecting relevant features...")
    selected_columns = [
        'Price', 'Production_year', 'Mileage_km', 'Power_HP', 'Displacement_cm3',
        'Fuel_type', 'Drive', 'Transmission', 'Type', 'Doors_number', 'Colour',
        'Vehicle_brand', 'Vehicle_model', 'Offer_publication_date', 'Currency'
    ]
    return df[selected_columns]

# ----------------------------
# 4. Handle Duplicates
# ----------------------------
def remove_duplicates(df):
    logger.info("Removing duplicates...")
    df['Offer_publication_date'] = pd.to_datetime(df['Offer_publication_date'], errors='coerce')
    df = df.sort_values(by='Offer_publication_date', ascending=False)
    df = df.drop_duplicates(
        subset=['Vehicle_brand', 'Vehicle_model', 'Production_year', 'Mileage_km'],
        keep='first'
    )
    df.reset_index(drop=True, inplace=True)
    logger.info(f"{len(df)} rows remain after removing duplicates.")
    return df

# ----------------------------
# 5. Currency Conversion
# ----------------------------
def convert_currency(df, rate=0.23):
    logger.info("Converting currency from PLN to EUR...")
    df.loc[df['Currency'] == 'PLN', 'Price'] *= rate
    return df

# ----------------------------
# 6. Clean Price Column
# ----------------------------
def clean_price_column(df):
    logger.info("Cleaning price column...")
    df['Price'] = df['Price'].apply(lambda x: "{:,.0f}".format(x))
    df['Price'] = df['Price'].str.replace(',', '')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    return df

# ----------------------------
# 7. Handle Missing Values
# ----------------------------
def impute_missing_values(df):
    logger.info("Handling missing values...")
    num_cols = ['Power_HP', 'Displacement_cm3', 'Doors_number']
    cat_cols = ['Drive', 'Transmission']

    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    logger.info("Missing values filled.")
    return df

# ----------------------------
# 8. Handle Outliers
# ----------------------------
def handle_outliers_multiple_columns(df, columns, threshold=3):
    logger.info("Handling outliers...")
    for column in columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            z_scores = (df[column] - df[column].mean()) / df[column].std()
            outliers = abs(z_scores) > threshold
            median_value = df[column].median()
            df.loc[outliers, column] = median_value
    return df

# ----------------------------
# Utility to get numerical columns
# ----------------------------
def get_numerical_columns(df):
    return df.select_dtypes(include=['int64', 'float64']).columns.tolist()
