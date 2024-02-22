from datetime import date
from wsgiref import validate


def init():
    today = date.today()
    getDate = today.strftime("%B %d, %Y")
    # print(getDate)

    validAmount = False
   
    while validAmount == False:
        try:
            amount = float(input("\nWhat's goood, me!! How much did we make today?? (" + getDate + ") >>  "))
        except ValueError:
            print("\nThat's not a number, fool! Try again.")
            continue
        else:
            print("We gooood")
            validAmount = True
            break
        

init()