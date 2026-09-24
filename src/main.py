from step1_extract import extract_weather_data
from step2_transform import transform_weather_data
from step3_load import load_to_database

def run_pipeline():
    """Run the full weather ETL pipeline: extract, transform, load."""
    print("Starting weather ETL pipeline...")
    
    raw_df = extract_weather_data()
    print(f"Extracted {len(raw_df)} row(s).")
    
    cleaned_df = transform_weather_data(raw_df)
    print(f"Transformed data - {cleaned_df.shape[1]} columns remaining.")
    
    load_to_database(cleaned_df)
    print("Pipeline finished successfully.")

if __name__ == "__main__":
    run_pipeline()