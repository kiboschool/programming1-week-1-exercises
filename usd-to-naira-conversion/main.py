# Program to calculate exchange rate
# Run interactively with python3 main.py

usd_value = float(input("Enter the amount of USD to convert to NGN: "))

NAIRA_PER_DOLLAR = 424.55 # Central bank exchange rate

ngn_value = usd_value * NAIRA_PER_DOLLAR

print(f"{usd_value:.2f} USD is {ngn_value:.2f} NGN")
