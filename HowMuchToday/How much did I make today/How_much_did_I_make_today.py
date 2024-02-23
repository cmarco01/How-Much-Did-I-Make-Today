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
            amount = round(amount)
            print("\nWe gooood, rounding to nearest dollar: $" + str(amount))
            validAmount = True
            break
    
        
    where = input("\n(OPTIONAL) From where? >> ")
    
    testDict = {
        getDate: {
            "amount" : amount,
            "where": where
        }
    }
    
    print(testDict)

    testDict.update({"amount":amount * 10, "where": "detroit"})
    
    print(testDict)
        

init()