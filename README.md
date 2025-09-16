# 📈 Stock Trading App using Polygon.io REST API

This project is a **Stock Trading App** that connects to the [Polygon.io](https://polygon.io/) REST API to fetch real-time stock ticker information. It demonstrates how to work with financial APIs, handle large paginated responses, and structure data for further analysis.

---

## 🚀 Features

- ✅ **Connecting to Polygon.io API** to pull **real-time stock ticker data**
- ✅ **Handling pagination** and API responses for large datasets
- ✅ **Structuring the data** with example ticker fields:
  - `ticker`, `name`, `market`, `exchange`, `type`, etc.
- ✅ **Writing the results to a CSV file** (`tickers.csv`) for analysis
- ✅ **Practicing real-world API integration workflows**
- ✅ **Designed to scale seamlessly** by handling API pagination (`next_url`) — capable of fetching **thousands of stock tickers**

---

## 🧰 Tech Stack

- **Python 3**
- [`requests`](https://pypi.org/project/requests/) – for making API calls
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) – for managing environment variables securely
- Python's built-in `csv` module – for exporting data

---

## ⚙️ How It Works

1. **Load API Key**
   - The API key is stored securely in a `.env` file:
     ```
     POLYGON_API_KEY=your_api_key_here
     ```

2. **Make API Call**
   - Fetches data from:
     ```
     https://api.polygon.io/v3/reference/tickers
     ```
   - Adds query parameters and your API key to retrieve tickers.

3. **Handle Pagination**
   - Continues requests using the `next_url` parameter until all pages are fetched.

4. **Structure and Save Data**
   - Extracts relevant fields from each ticker.
   - Saves the structured data to `tickers.csv`.

---

## 📂 Project Structure

