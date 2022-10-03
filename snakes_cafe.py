
import pandas as pd

menu='''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Beverages
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************'''
other_menu = [
        "quit",
        "wings",
        "cookies",
        "spring rolls",
        "salmon",
        "steak",
        "meat tornado",
        "a literal garden",
        "ice cream",
        "cake",
        "pie",
        "coffee",
        "tea",
        "unicorn tears"
]


def choose_order ():
    list=[]

    counter=0
    while True:
        order = input("> ")
        if order in other_menu:
        
         if order == "quit":
            if len(list)>1 :
                count = pd.Series(list).value_counts()
                print("your order is ")
                print("meal  Count")
                print (count)
            break
            
         else:

           list.append(order)
           
           if order in list:
               counter =list.count(order)
           print(f"** {counter} order of {order} have been added to your meal **")
          
        else:
            print("your order not found")

           

        
           


if __name__=="__main__":
    
    
    print(menu)
    choose_order()