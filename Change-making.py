import sys

if len(sys.argv) == 2:
    money = sys.argv[1]
    try:
        value = float(money)
        if value > 0:
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
        print("1) Standard USD? \n2) Prime Numbers up to the input? \n3) Manually input a list of coin values?")
        coin_selection = input()
        
        if coin_selection in ["1","2","3"]:
            has_chosen = True
        else:
            print("Please select a valid coin option, '1', '2', or '3'")

        if coin_selection == "1":
            coins = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
        elif coin_selection == "2":
            coins = []
            print("primes still needs to be setup")
            sys.exit()
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









