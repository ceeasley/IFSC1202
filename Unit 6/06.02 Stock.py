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

