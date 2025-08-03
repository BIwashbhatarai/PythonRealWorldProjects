# Import the requests library to make HTTP requests
import requests

# Your ExchangeRate-API key (get one for free from exchangerate-api.com)
API_KEY = "Your_API_Key"

# Ask user which currency they are converting from (like USD)
from_currency = input("From currency (e.g. USD): ").upper()

# Ask user which currency they are converting to (like NPR)
to_currency = input("To currency (e.g. NPR): ").upper()

# Ask user how much money they want to convert
amount = float(input("Amount to convert: "))

# Create the URL to fetch exchange rates based on 'from_currency'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

# Send a GET request to the API and get the response
response = requests.get(url)

# Convert the response to JSON (dictionary format)
data = response.json()

# Get the exchange rate from the API data
rate = data["conversion_rates"][to_currency]

# Multiply the amount by the exchange rate to get converted value
converted = amount * rate

# Print the final result with 2 decimal places
print(f"\n💱 {amount} {from_currency} = {converted:.2f} {to_currency}")
