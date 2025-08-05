import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine } from 'recharts';

const PriceChart = ({ prices, changePoints, events, indicators }) => {
  const data = prices.dates?.map((date, index) => {
    const vol = indicators.volatility.find(v => v.date === date);
    return {
      date,
      price: prices.prices[index],
      volatility: vol ? vol.volatility : null
    };
  });

  return (
    <div className="bg-white p-4 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-4">Brent Oil Prices with Change Points and Events</h2>
      <LineChart
        width={window.innerWidth < 768 ? window.innerWidth - 40 : 800}
        height={400}
        data={data}
        margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis yAxisId="left" label={{ value: 'Price (USD)', angle: -90, position: 'insideLeft' }} />
        <YAxis yAxisId="right" orientation="right" label={{ value: 'Volatility', angle: 90, position: 'insideRight' }} />
        <Tooltip />
        <Legend />
        <Line yAxisId="left" type="monotone" dataKey="price" stroke="#8884d8" name="Brent Oil Price" />
        <Line yAxisId="right" type="monotone" dataKey="volatility" stroke="#82ca9d" name="30-Day Volatility" />
        {changePoints.map(cp => (
          <ReferenceLine
            key={cp.date}
            x={cp.date}
            stroke="red"
            label={{ value: `Change Point: ${cp.date}`, position: 'top', fill: 'red' }}
          />
        ))}
        {events.map(event => (
          <ReferenceLine
            key={event.date}
            x={event.date}
            stroke="green"
            label={{ value: event.event, position: 'top', fill: 'green' }}
          />
        ))}
      </LineChart>
      <h3 className="text-lg font-semibold mt-4">Change Point Details</h3>
      {changePoints.map(cp => (
        <div key={cp.date} className="mt-2">
          <p><strong>Change Point:</strong> {cp.date}</p>
          <p><strong>Mean Price Before:</strong> ${cp.mean_before.toFixed(2)}</p>
          <p><strong>Mean Price After:</strong> ${cp.mean_after.toFixed(2)}</p>
          <p><strong>Percentage Change:</strong> {cp.percent_change.toFixed(2)}%</p>
        </div>
      ))}
      <h3 className="text-lg font-semibold mt-4">Price Changes Around Events</h3>
      {indicators.price_changes?.map(pc => (
        <div key={pc.date} className="mt-2">
          <p><strong>Event:</strong> {pc.event} ({pc.date})</p>
          <p><strong>Average Price Change (±5 days):</strong> {pc.avg_price_change.toFixed(2)}%</p>
        </div>
      ))}
    </div>
  );
};

export default PriceChart;