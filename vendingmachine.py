amount = 0
while True:
    money = input("\n :::: Please Enter Money to buy Soda =>  ")
    if(money == 25 or money == 100 ):
        amount += money
        if(amount >= 125): 
            amount -= 125
            print "\nYour Soda is ready and rest of your ",amount," Rs\n"
            exit()
    else:
        print "\nCoins other than 25 and 100 are not acceptable\n"
        print "\nYour money back",money," Rs \n"