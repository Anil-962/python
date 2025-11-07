# stocks.csv contains stock price, earnings per share and book value. 
# You are writing a stock market application that will process this file and 
# create a new file with financial metrics such as pe ratio and price to book ratio. 
# These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value

with open("stocks.csv","r") as f,open("output.csv","w") as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")
    next(f)
    
    for line in f:
        tokens  = line.split(',')
        stocks = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        books = float(tokens[3])
        pe = price / eps
        pb = price / books
        out.write(f"{stocks},{pe},{pb}\n")