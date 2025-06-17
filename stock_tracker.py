stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "RIL": 1431,
    "HDFC": 3840,
    "Airtel": 1856,
    "ICICI": 1417,
    "Infosys": 1612,
    "ITC": 417,
    "L&T" : 3610,
    "TCS": 3506,
    "SBI": 793,
    "Sun Pharma": 1678,
    "Oracle": 9709,
    "Mphasis": 2701,
    "HCL": 1726,
    "HAL": 5057,
    "Wipro": 261,
    "DLF": 857,
    "Adani": 992,
    "ONGC": 254,
    "Eicher": 5370,
    "Bosch": 32240
      
    
}

portfolio = {}

while True:
    stock = input("enter stock symbol or 'Done' :").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("STOCK NOT FOUND")
        continue
    
    quantity = int(input("enter quantity:")).upper()
    portfolio[stock] = quantity
    
    total_value = 0
    print("your stock portfolio").upper()
    for stock , quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value
        print(f"{stock}: {quantity} shares *  ${price} = ${value}")
    
    print(f"\n💰 Total Portfolio Value: ${total_value}") 
      

choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("📈 Stock Portfolio Summary\n\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\n💰 Total Portfolio Value: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'.")
else:
    print("❌ Portfolio not saved.")

        
    
    
    