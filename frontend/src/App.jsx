import { useEffect, useState } from "react";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell, Legend
} from "recharts";
import {
  getSummary, getCityData, getCategoryData, getSourceData, getListings
} from "./api";

const chartColors = ["#4f46e5", "#0ea5e9", "#10b981", "#f59e0b", "#ec4899", "#8b5cf6"];

function StatCard({ title, value }) {
  return (
    <div className="stat-card">
      <p>{title}</p>
      <h2>{value ?? 0}</h2>
    </div>
  );
}

function App() {
  const [summary, setSummary] = useState({});
  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);
  const [listings, setListings] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadDashboard(searchText = "") {
    try {
      setError("");
      const [summaryResult, cities, categories, sources, listingRows] = await Promise.all([
        getSummary(), getCityData(), getCategoryData(), getSourceData(), getListings(searchText)
      ]);
      setSummary(summaryResult);
      setCityData(cities);
      setCategoryData(categories);
      setSourceData(sources);
      setListings(listingRows);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadDashboard();
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => loadDashboard(search), 300);
    return () => clearTimeout(timer);
  }, [search]);

  return (
    <div className="page">
      <header className="topbar">
        <div>
          <span className="eyebrow">BUSINESS INTELLIGENCE</span>
          <h1>Business Listings Dashboard</h1>
          <p>Explore business listings by city, category, and source.</p>
        </div>
        <button className="refresh-button" onClick={() => loadDashboard(search)}>Refresh data</button>
      </header>

      {error && (
        <div className="message error">
          {error} Make sure MySQL and the FastAPI backend are running.
        </div>
      )}
      {loading && <div className="message">Loading dashboard...</div>}

      <section className="stats-grid">
        <StatCard title="Total listings" value={summary.total_listings} />
        <StatCard title="Cities" value={summary.total_cities} />
        <StatCard title="Categories" value={summary.total_categories} />
        <StatCard title="Sources" value={summary.total_sources} />
      </section>

      <section className="charts-grid">
        <div className="panel">
          <div className="panel-heading">
            <div><h2>City-wise listings</h2><p>Number of businesses in each city</p></div>
          </div>
          <div className="chart-area">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={cityData} margin={{ top: 10, right: 10, left: 0, bottom: 10 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} />
                <XAxis dataKey="name" tick={{ fontSize: 12 }} />
                <YAxis allowDecimals={false} />
                <Tooltip />
                <Bar dataKey="count" name="Businesses" fill="#4f46e5" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="panel">
          <div className="panel-heading">
            <div><h2>Category distribution</h2><p>Listings grouped by category</p></div>
          </div>
          <div className="chart-area">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={categoryData} dataKey="count" nameKey="name" cx="50%" cy="48%"
                  outerRadius={105} label>
                  {categoryData.map((entry, index) => (
                    <Cell key={entry.name} fill={chartColors[index % chartColors.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      <section className="panel source-panel">
        <div className="panel-heading">
          <div><h2>Source-wise listings</h2><p>Where the records came from</p></div>
        </div>
        <div className="source-list">
          {sourceData.map((item, index) => (
            <div className="source-row" key={item.name}>
              <div className="source-label"><span className="dot" style={{ background: chartColors[index % chartColors.length] }} />{item.name}</div>
              <strong>{item.count}</strong>
            </div>
          ))}
          {sourceData.length === 0 && <p className="empty">No source data available.</p>}
        </div>
      </section>

      <section className="panel table-panel">
        <div className="table-heading">
          <div><h2>Business listings</h2><p>Search by business name, category, or city</p></div>
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Search listings..."
            aria-label="Search listings"
          />
        </div>
        <div className="table-wrap">
          <table>
            <thead>
              <tr><th>Business name</th><th>Category</th><th>City</th><th>Address</th><th>Phone</th><th>Source</th></tr>
            </thead>
            <tbody>
              {listings.map((item) => (
                <tr key={item.id}>
                  <td className="business-name">{item.business_name}</td>
                  <td>{item.category}</td>
                  <td>{item.city}</td>
                  <td>{item.address || "—"}</td>
                  <td>{item.phone || "—"}</td>
                  <td><span className="source-tag">{item.source}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
          {listings.length === 0 && <p className="empty">No listings found.</p>}
        </div>
      </section>

      <footer>React + FastAPI + MySQL · Student assignment project</footer>
    </div>
  );
}

export default App;
