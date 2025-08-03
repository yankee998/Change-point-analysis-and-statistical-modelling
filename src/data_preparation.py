import pandas as pd
import numpy as np

def load_brent_data(file_path):
    """Load and preprocess Brent oil price data."""
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
        df = df.sort_values('Date').dropna()
        df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
        print(f"Loaded and processed Brent oil data: {df.shape[0]} rows")
        return df
    except Exception as e:
        print(f"Error loading Brent data: {e}")
        return None

def compile_events(output_path='data/processed/events.csv'):
    """Compile a dataset of major events affecting oil prices."""
    try:
        events = [
            {'Date': '1990-08-02', 'Event': 'Gulf War Begins', 'Category': 'Geopolitical'},
            {'Date': '2003-03-20', 'Event': 'Iraq War Starts', 'Category': 'Geopolitical'},
            {'Date': '2008-09-15', 'Event': 'Global Financial Crisis', 'Category': 'Economic'},
            {'Date': '2011-02-15', 'Event': 'Arab Spring Begins', 'Category': 'Geopolitical'},
            {'Date': '2014-11-27', 'Event': 'OPEC Maintains Production Levels', 'Category': 'OPEC'},
            {'Date': '2016-11-30', 'Event': 'OPEC Production Cut Agreement', 'Category': 'OPEC'},
            {'Date': '2020-03-06', 'Event': 'OPEC+ Price War', 'Category': 'Economic'},
            {'Date': '2011-10-27', 'Event': 'Libya Conflict Intensifies', 'Category': 'Geopolitical'},
            {'Date': '2014-06-01', 'Event': 'ISIS Captures Iraqi Oil Fields', 'Category': 'Geopolitical'},
            {'Date': '2018-05-08', 'Event': 'US Withdraws from Iran Nuclear Deal', 'Category': 'Geopolitical'},
            {'Date': '2020-01-03', 'Event': 'US-Iran Tensions Escalate', 'Category': 'Geopolitical'},
            {'Date': '2001-09-11', 'Event': '9/11 Attacks', 'Category': 'Geopolitical'},
            {'Date': '1991-01-17', 'Event': 'Operation Desert Storm', 'Category': 'Geopolitical'},
            {'Date': '2015-12-04', 'Event': 'OPEC Fails to Agree on Production Cut', 'Category': 'OPEC'},
            {'Date': '2019-09-14', 'Event': 'Saudi Aramco Drone Attack', 'Category': 'Geopolitical'}
        ]
        events_df = pd.DataFrame(events)
        events_df['Date'] = pd.to_datetime(events_df['Date'], format='%Y-%m-%d')
        events_df.to_csv(output_path, index=False)
        print(f"Events dataset saved to {output_path}: {len(events)} events")
        return events_df
    except Exception as e:
        print(f"Error compiling events: {e}")
        return None

if __name__ == "__main__":
    # Define file paths
    brent_file = "C:/Users/Skyline/Change point analysis and statistical modelling/data/raw/BrentOilPrices.csv"
    events_file = "C:/Users/Skyline/Change point analysis and statistical modelling/data/processed/events.csv"
    
    # Load and preprocess Brent oil data
    brent_df = load_brent_data(brent_file)
    if brent_df is not None:
        print("Brent Data Preview:")
        print(brent_df.head())
    
    # Compile events
    events_df = compile_events(events_file)
    if events_df is not None:
        print("Events Data Preview:")
        print(events_df.head())