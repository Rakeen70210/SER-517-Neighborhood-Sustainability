import logo from './logo.svg';
import './App.css';
import Chart from './components/Chart/Chart.jsx';
import SearchBar from './components/SearchBar';
import cities from './static_data/final500CitiesLimited.json';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        Neighborhood Sustainability Project
        <SearchBar
          top500Cities={cities}
          placeholder="Enter a city"
        />
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
      <div className="chartPanel">
        <Chart />
      </div>
    </div>
  );
}

export default App;
