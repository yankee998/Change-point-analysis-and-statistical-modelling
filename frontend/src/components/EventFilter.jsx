import React, { useState } from 'react';

const EventFilter = ({ onFilter }) => {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onFilter(startDate, endDate);
  };

  return (
    <div className="bg-white p-4 rounded-lg shadow-md mb-4">
      <h2 className="text-xl font-semibold mb-4">Filter Events by Date Range</h2>
      <div className="flex flex-col md:flex-row gap-4">
        <label className="flex-1">
          <span className="block text-sm font-medium">Start Date:</span>
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            className="mt-1 p-2 border rounded w-full"
          />
        </label>
        <label className="flex-1">
          <span className="block text-sm font-medium">End Date:</span>
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            className="mt-1 p-2 border rounded w-full"
          />
        </label>
        <div className="flex gap-2 mt-4">
          <button
            type="submit"
            onClick={handleSubmit}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Apply Filter
          </button>
          <button
            type="button"
            onClick={() => { setStartDate(''); setEndDate(''); onFilter('', ''); }}
            className="bg-gray-300 px-4 py-2 rounded hover:bg-gray-400"
          >
            Clear Filter
          </button>
        </div>
      </div>
    </div>
  );
};

export default EventFilter;