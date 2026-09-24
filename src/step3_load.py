import sqlite3
import pandas as pd

def load_to_database(df, db_path='data/weather.db', table_name='weather'):
    """Append a DataFrame into a SQLite database table, preserving existing data."""
    
    # Connect to (or create, if it doesn't exist yet) the database file
    conn = sqlite3.connect(db_path)
    
    # if_exists='append' adds new rows on top of existing data instead of
    # overwriting the table - this is what builds up weather history over time
    # (different from Project 3, which used 'replace' to wipe and reload each time)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    # Always close the connection after writing, to avoid locking the database file
    conn.close()
    
    print(f"Appended {len(df)} row(s) into '{table_name}' table in {db_path}")

# Quick test when running this file directly
if __name__ == "__main__":
    from step1_extract import extract_weather_data
    from step2_transform import transform_weather_data
    
    # Run the full extract -> transform pipeline once, then load the result
    raw_df = extract_weather_data()
    cleaned_df = transform_weather_data(raw_df)
    load_to_database(cleaned_df)