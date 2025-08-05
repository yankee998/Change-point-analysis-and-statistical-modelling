import React from 'react';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-2xl font-bold text-center">Brent Oil Price Analysis Dashboard</h1>
      </header>
      <Dashboard />
    </div>
  );
}

export default App;