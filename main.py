from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
import os

warnings.filterwarnings("ignore")

portfolio = []

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def addStock(name, ticker, sector, numOfShares):
    price = round(float(stock_info.get_live_price(ticker)), 2)
    newStock = Stock(name, ticker, sector, price, numOfShares)
    portfolio.append(newStock)
    print(f"Successfully added {name} ({ticker}) to the portfolio.")

def updatePrices():
    for stock in portfolio:
        price = stock_info.get_live_price(stock.ticker)
        stock.currentPrice = round(float(price), 2)

def calculate_gain_loss(stock):
    initial_value = stock.originalPrice * stock.numOfShares
    current_value = stock.currentPrice * stock.numOfShares
    return round(current_value - initial_value, 2)

def viewPortfolio():
    clear_terminal()
    print("{:<20}{:<10}{:<20}{:<10}{:<10}{:<10}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    print("=" * 80)
    for count, stock in enumerate(portfolio, start=1):
        gain_loss = calculate_gain_loss(stock)
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{20}} {("$" + str(stock.currentPrice))} {stock.numOfShares:{4}}{gain_loss:{10}}")

def searchBySector():
    clear_terminal()
    sector = input("Enter the sector to search for: ").strip().lower()
    results = [stock for stock in portfolio if stock.sector.lower() == sector]

    if results:
        print("{:<20}{:<10}{:<20}{:<10}{:<10}{:<10}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
        print("=" * 80)
        for count, stock in enumerate(results, start=1):
            gain_loss = calculate_gain_loss(stock)
            print(f"{count:<20}{stock.name:<10}{stock.ticker:<20}{stock.sector:<10}${stock.currentPrice:<10.2f}{stock.numOfShares:<10}{gain_loss:<10.2f}")
    else:
        print("No stocks found in this sector.")

def mainMenu():
    print("\nMain Menu")
    print("1. Add a new stock to the portfolio")
    print("2. Update Stock Prices")
    print("3. Search by Sector")
    print("4. View portfolio")
    print("5. Exit program")

def main():
    clear_terminal()
    print("Welcome to My Stock Portfolio")

    while True:
        mainMenu()
        choice = input("\nSelect from the following options: ").strip()
        clear_terminal()

        if choice == "1":
            name = input("Enter the Name of the Stock: ").strip()
            ticker = input("Enter the stock ticker name: ").strip()
            tick = yf.Ticker(ticker).info
            sector = tick.get("industry", "Unknown")
            numOfShares = int(input("Enter number of stock shares to buy: ").strip())
            addStock(name, ticker, sector, numOfShares)
        elif choice == "2":
            updatePrices()
            print("Prices updated.")
        elif choice == "3":
            searchBySector()
        elif choice == "4":
            viewPortfolio()
        elif choice == "5":
            print("Thanks for using my stock portfolio program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
