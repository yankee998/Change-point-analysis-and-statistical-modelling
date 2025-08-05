import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PriceChart from './PriceChart';
import EventFilter from './EventFilter';

const Dashboard = () => {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [events, setEvents] = useState([]);
  const [filteredEvents, setFilteredEvents] = useState([]);
  const [indicators, setIndicators] = useState({ volatility: [], price_changes: [] });

  useEffect(() => {
    axios.get('http://localhost:5000/api/prices')
      .then(response => setPrices(response.data))
      .catch(error => console.error('Error fetching prices:', error));

    axios.get('http://localhost:5000/api/change_points')
      .then(response => setChangePoints(response.data))
      .catch(error => console.error('Error fetching change points:', error));

    axios.get('http://localhost:5000/api/events')
      .then(response => {
        setEvents(response.data);
        setFilteredEvents(response.data);
      })
      .catch(error => console.error('Error fetching events:', error));

    axios.get('http://localhost:5000/api/indicators')
      .then(response => setIndicators(response.data))
      .catch(error => console.error('Error fetching indicators:', error));
  }, []);

  const handleFilter = (startDate, endDate) => {
    if (!startDate || !endDate) {
      setFilteredEvents(events);
      return;
    }
    const filtered = events.filter(event => {
      const eventDate = new Date(event.date);
      return eventDate >= new Date(startDate) && eventDate <= new Date(endDate);
    });
    setFilteredEvents(filtered);
  };

  return (
    <div className="container mx-auto p-4">
      <EventFilter onFilter={handleFilter} />
      <PriceChart prices={prices} changePoints={changePoints} events={filteredEvents} indicators={indicators} />
    </div>
  );
};

export default Dashboard;