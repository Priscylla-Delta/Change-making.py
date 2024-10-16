import sys
import math


def main():

    input = validate_input()
    coins = choose_coins(input)
    used_Coins = make_change(input, coins)
    print_change(used_Coins)
    return


def validate_input():
    if len(sys.argv) == 2:
        input = sys.argv[1]
        try:
            input = round(float(input),ndigits=2) #cuts the input to 2 sd
            if input > 0:
                pass
            else:
                print("Posative numbers only")
                sys.exit()
        except ValueError:
            print("Only Numbers")
            sys.exit()
    else:
        print("Correct use 'Change-making.py <Amount of Money>")
        sys.exit()       

    return input 


def choose_coins(max):
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
            coins = create_prime_coins(max)

        else: 
            coins = create_manual_coins()

    return coins

def create_prime_coins(input):
     #chat, I have no idea how this works, but it does, so thats neat
        # Method 5 : https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
    
    coins = list()
    limit = math.floor(input)
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if (sieve[p]):
            coins.append(p)
            for i in range(p, limit + 1, p):
                sieve[i] = False

    extra_coins = [.25, .1, .05, .01]
    for extra in extra_coins:
        coins.append(extra)

    coins.sort(reverse=True)

    return coins

def create_manual_coins():
    coins = [.01]
    
    done = False
    while done == False:
        print("Input the value of a coin you would like to use? or Type 'Done' to continue")
        coin = input()
        if str(coin.lower()) == "done":
            coins.sort(reverse=True)
            return coins
        try:
            coin = round(float(coin), ndigits=2)
            if coin > 0:
                coins.append(coin)
            else:
                print("Posative numbers only")

        except ValueError:
            print("Only Numbers")




def make_change(input, coins):
    used_Coins = []
    i = 0
    while input > 0:
        if coins[i] <= input:
            input = round(input - (coins[i]), ndigits=2)
            used_Coins.append(coins[i])

        else:
            i += 1

    return used_Coins
    

def print_change(used_Coins):
    counts = {}
    for used_Coin in used_Coins:
        count = used_Coins.count(used_Coin)
        counts[used_Coin] = count

    for coin in counts:
        print(coin, "was used", counts[coin], "times")

    
    return


main()