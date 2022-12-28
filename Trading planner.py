#type tts() in the console to begin the planner

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price ')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    ''' takes a list of 1 or more prices and computes and returns the average price'''
    result=0
    for i in prices:
        result+=i
    return result/len(prices)
def min_day(prices):
    ''' takes a list of 1 or more prices and computes and returns the day (i.e., the index) of the minimum price'''
    result=0
    for i in range(len(prices)):
        if prices[i]<prices[result]:
            result=i
            
    return result
def max_change_day(prices):
    '''takes a list of 2 or more prices and computes and returns the day (i.e., the index) of the maximum single-day change in price'''
    result=0
    value=0
    for i in range(1,len(prices)):
        if prices[i]-prices[i-1]>value:
            result=i
            value+=prices[result]-prices[result-1]
          
         
    return result    
def any_above(prices,threshold):
    '''any_above that takes a list of 1 or more prices and an integer threshold, and uses a loop to determine if there are any prices above that threshold'''
    for i in range(len(prices)):
        if prices[i]>threshold:
            return True
            break
    if prices[i]<threshold:
            return False
def find_tts(prices):
    '''takes a list of 2 or more prices, and that uses one or more loops to find the best days on which to buy and sell the stock whose prices are given in the list of prices'''
    maxdiff=0
    pos1=0
    pos2=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            d=prices[j]-prices[i]
            if d>maxdiff:
                maxdiff=d
                pos1=i
                pos2=j  
    return[pos1,pos2,maxdiff]

def tts():
    """ the main user-interaction loop
    """
    prices = []
    threshold=''
    pos1=0
    po2=0
    maxdiff=0

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        
        ## add code to process the other choices here'
        elif choice == 3:
            avg_prices = avg_price(prices)
            print('The average price is', avg_prices)
        elif choice ==4:
         
            result=min_day(prices)
            print('the min price is',prices[result],'on day',result)
        elif choice==5:
          result=max_change_day(prices)
          
          print('The max single-day change occurs on day',result,'when the price goes from',prices[result-1],'to',prices[result])
        elif choice==6:
            threshold = eval(input('Enter the threshold:'))
            result=any_above(prices,threshold)
            if result==True:
                print('There is at least one price above',threshold)
            if result==False:
                print('There are no prices above',threshold)
           
            any_above(prices,threshold)
        elif choice==7:
            result=find_tts(prices)
            print('Buy on day',result[0],'at price',prices[result[0]])
            print('Sell on day',result[1],'at price',prices[result[1]])
            print('Total profit:',result[2])
        

            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
