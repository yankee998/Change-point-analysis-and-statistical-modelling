from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

def load_data():
    """Load and preprocess Brent oil prices and events."""
    prices_df = pd.read_csv('C:/Users/Skyline/Change point analysis and statistical modelling/data/raw/BrentOilPrices.csv')
    prices_df['Date'] = pd.to_datetime(prices_df['Date'], format='mixed', dayfirst=True)
    prices_df = prices_df.sort_values('Date')
    
    events_df = pd.read_csv('C:/Users/Skyline/Change point analysis and statistical modelling/data/events/oil_market_events.csv')
    events_df['Date'] = pd.to_datetime(events_df['Date'], format='%Y-%m-%d')
    return prices_df, events_df

@app.route('/api/prices', methods=['GET'])
def get_prices():
    """Return Brent oil prices as JSON."""
    prices_df, _ = load_data()
    data = {
        'dates': prices_df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        'prices': prices_df['Price'].tolist()
    }
    return jsonify(data)

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    """Return change point analysis results."""
    change_points = [
        {
            'date': '2005-02-24',
            'index': 4521,
            'mean_before': 21.44,
            'mean_after': 75.58,
            'percent_change': 252.49
        }
    ]
    return jsonify(change_points)

@app.route('/api/events', methods=['GET'])
def get_events():
    """Return oil market events."""
    _, events_df = load_data()
    data = [
        {'date': row['Date'].strftime('%Y-%m-%d'), 'event': row['Event'], 'description': row['Description']}
        for _, row in events_df.iterrows()
    ]
    return jsonify(data)

@app.route('/api/indicators', methods=['GET'])
def get_indicators():
    """Return volatility and average price changes around events."""
    prices_df, events_df = load_data()
    prices_df['Volatility'] = prices_df['Price'].rolling(window=30).std()
    volatility = [
        {'date': row['Date'].strftime('%Y-%m-%d'), 'volatility': row['Volatility']}
        for _, row in prices_df.iterrows() if not pd.isna(row['Volatility'])
    ]
    
    price_changes = []
    for _, event in events_df.iterrows():
        event_date = event['Date']
        window = prices_df[
            (prices_df['Date'] >= event_date - pd.Timedelta(days=5)) &
            (prices_df['Date'] <= event_date + pd.Timedelta(days=5))
        ]
        if not window.empty:
            avg_change = window['Price'].pct_change().mean() * 100
            price_changes.append({
                'event': event['Event'],
                'date': event_date.strftime('%Y-%m-%d'),
                'avg_price_change': avg_change if not pd.isna(avg_change) else 0
            })
    
    return jsonify({'volatility': volatility, 'price_changes': price_changes})

if __name__ == '__main__':
    app.run(debug=True, port=5000)