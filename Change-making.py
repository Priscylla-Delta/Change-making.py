from decimal import Decimal


money = 100.58

coins = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]

#print(coins)



used_Coins = []
i = 0
while money > 0:
    if coins[i] <= money:
        money = round(money - (coins[i]), ndigits=2)
        used_Coins.append(coins[i])
        ## print(money)
        ## print(coins[i])
    else:
        i += 1


counts = {}
for used_Coin in used_Coins:
    count = used_Coins.count(used_Coin)
    counts[used_Coin] = count
    #print(used_Coin, "was used", count, "times")

for coin in counts:
    print(coin, "was used", counts[coin], "times")


#print(counts)
print("Leftover money =" , money)









