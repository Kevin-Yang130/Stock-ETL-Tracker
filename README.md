# Stock/ETF Data Tracker 

A Python-based tool for fetching, visualizing, and delivering real-time stock and ETF data. This project utilizes the Yahoo Finance API (`yfinance`) to retrieve historical market data and delivers daily financial updates via email. The tool also generates insightful visualizations for better data interpretation.

## Features 
- **Real-Time Market Data**: Fetches stock and ETF data using the `yfinance` library.
- **Email Notifications**: Sends tabulated financial summaries directly to your email with secure SMTP authentication.
- **Data Visualization**: Creates and saves professional plots of closing prices using `matplotlib`.
- **User-Friendly**: Easy-to-use script that prompts for inputs and delivers results efficiently.
- **Secure**: Protects user credentials with `getpass` and ensures secure TLS encryption.

## Technologies Used 
- **Python**: Core programming language
- **yfinance**: Fetching financial data
- **Pandas & NumPy**: Data processing and manipulation
- **Matplotlib**: Visualization of stock trends
- **smtplib & getpasslib**: Email automation and secure authentication

## How It Works 
1. Input a stock/ETF ticker symbol.
2. Fetch historical data for the past month.
3. Generate an HTML email with financial summaries.
4. Visualize and save a plot of the closing prices.

## Getting Started
Clone the repository, install the dependencies, and run the script:

```bash
git clone https://github.com/your-username/stock-etf-data-tracker.git
cd stock-etf-data-tracker
pip install -r requirements.txt
python stock_etf_tracker.py
