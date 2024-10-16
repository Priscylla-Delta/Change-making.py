


money = 10

coins = [1,2,3,4,5]
coins.reverse()
print(coins)




i = 0
while money > 0:
    if coins[i] <= money:
        money = money - coins[i]
        print(coins[i])
    else:
        i += 1



print("Leftover money =" , money)









