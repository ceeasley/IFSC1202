#You have a file that has the stock prices for a week, one per line.
#Create a program that performs the following:
#    Defines a function called "percentchange"
#        Accepts today stock price (floating point) and yesterdays stock price (floating point) as parameters
#        Calculates and percent change between yesterdays and todays stockprice
#            Percent Change is todays stock value - yesterdays stock value divided by yesterdays stock value time 100
#Opens and reads the first line of 06.02 Stock.txt file
#Prints headings and the first stock value (there is no percent change on the first day)
#Reads the next line of input
#Calculates and prints the stock value and the percent change from yesterday. Each column is 10 characters wide with a space between them.

def percentchange(yesterday, today):
    if yesterday != 0:
        change = float(((today - yesterday)/yesterday)*100)
        return change
    else:
        return None

price_today = 0
price_yest = 0

with open("06.02 Stock.txt") as prices:
    price = prices.readline()
    print(f'{"Price":^10} {"Change":^10}')

    while price:
        price_yest = price_today
        price_today = float(price)
        percent = percentchange(price_yest, price_today)
        if percent != None:
            print(f'{price_today:10.2f} {percent:10.2f}')
        else:
            print(f'{price_today:10.2f}')
        price = prices.readline()

