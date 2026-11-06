const API_URL = "http://127.0.0.1:8000/api";

async function getData(path) {
  const response = await fetch(`${API_URL}${path}`);
  if (!response.ok) {
    throw new Error("Could not load data from the backend.");
  }
  return response.json();
}

export function getSummary() {
  return getData("/dashboard/summary");
}

export function getCityData() {
  return getData("/dashboard/city-wise");
}

export function getCategoryData() {
  return getData("/dashboard/category-wise");
}

export function getSourceData() {
  return getData("/dashboard/source-wise");
}

export function getListings(search = "") {
  const params = new URLSearchParams({ limit: "100" });
  if (search.trim()) params.set("search", search.trim());
  return getData(`/listings?${params.toString()}`);
}
