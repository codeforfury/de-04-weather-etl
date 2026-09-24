import pandas as pd

def transform_weather_data(df):
    """Clean the raw weather DataFrame: fix data types, drop unnecessary columns."""
    
    # Convert time from text to proper datetime
    df['time'] = pd.to_datetime(df['time'])
    
    # Drop interval column - metadata about the reading, not actual weather data
    df = df.drop(columns=['interval'])
    
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    from step1_extract import extract_weather_data
    
    raw_df = extract_weather_data()
    cleaned_df = transform_weather_data(raw_df)
    
    print(cleaned_df.dtypes)
    print(cleaned_df)