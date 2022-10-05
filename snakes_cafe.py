
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
        "Quit",
        "Wings",
        "Cookies",
        "",
        "Salmon",
        "Steak",
        "Meat Tornado",
        "A Literal Garden",
        "Ice Cream",
        "Cake",
        "Pie",
        "Coffee",
        "Tea",
        "Unicorn Tears"
]


def choose_order ():
    list=[]

    counter=0
    while True:
        order = (input("> ").title())
        if order in other_menu:
        
         if order == "Quit":
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