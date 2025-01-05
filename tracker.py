import yfinance as yf
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    """Fetch historical stock data for a given ticker symbol."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")  # Fetch last month's data
    return hist

def generate_email_content(ticker, data):
    """Generate an HTML email with the stock data."""
    html_content = f"""
    <html>
        <body>
            <h2>Stock/ETF Data for {ticker}</h2>
            {data.to_html()}
        </body>
    </html>
    """
    return html_content

def send_email(recipient_email, subject, body):
    """Send an email with the stock data."""
    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass("Enter your Gmail password: ")

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Start TLS encryption

    try:
        server.login(sender_email, sender_password)

        # Create the email
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg.attach(MIMEText(body, "html"))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

def plot_stock_data(ticker, data):
    """Plot the stock's closing prices over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b')
    plt.title(f"{ticker} Closing Prices (Last Month)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.savefig(f"{ticker}_chart.png")
    plt.show()

def main():
    print("Welcome to the Stock/ETF Data Tracker!")
    ticker = input("Enter the ticker symbol for the stock/ETF: ").upper()

    try:
        # Fetch stock data
        data = fetch_stock_data(ticker)

        # Generate and save a visualization
        plot_stock_data(ticker, data)

        # Generate tabulated data for email
        tabulated_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

        # Generate email content
        email_body = generate_email_content(ticker, tabulated_data)

        # Send email
        recipient_email = input("Enter the recipient's email address: ")
        send_email(recipient_email, subject=f"Daily Stock/ETF Data for {ticker}", body=email_body)

        print("Task completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
