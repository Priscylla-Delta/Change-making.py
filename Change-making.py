import sys
import math

if len(sys.argv) == 2:
    money = sys.argv[1]
    try:
        money = round(float(money),ndigits=2) #cuts the input to 2 sd
        if money > 0:
            pass
        else:
            print("Posative numbers only")
            sys.exit()
    except ValueError:
        print("Only Numbers")
        sys.exit()

    print("Making Change for ", sys.argv[1], "\n What type of coins would you like to use?")

    has_chosen = False
    while has_chosen == False:
        print("1) Standard USD? \n2) Prime Numbers up to the input? (This selection will use Standard USD for any decimal values)\n3) Manually input a list of coin values?")
        coin_selection = input()
        
        if coin_selection in ["1","2","3"]:
            has_chosen = True
        else:
            print("Please select a valid coin option, '1', '2', or '3'")

        if coin_selection == "1":
            coins = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
        elif coin_selection == "2":
            coins = []
            #print("primes still needs to be setup")


            #chat, I have no idea how this works, but it does, so thats neat
                # Method 5 : https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
            coins = list()
            limit = math.floor(money)
            sieve = [True] * (limit + 1)
            for p in range(2, limit + 1):
                if (sieve[p]):
                    coins.append(p)
                    for i in range(p, limit + 1, p):
                        sieve[i] = False

            decimal_coins = [.25, .1, .05, .01]
            for extra in decimal_coins:
                coins.append(extra)

            coins.sort(reverse=True)
            # print(coins)
    
        else: 
            coins = []
            print("Manual still needs to be setup")
            sys.exit()


else: 
    print("Correct use 'Change-making.py <Amount of Money>")
    sys.exit()




used_Coins = []
i = 0
while money > 0:
    if coins[i] <= money:
        money = round(money - (coins[i]), ndigits=2)
        used_Coins.append(coins[i])
        # print(money)
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









