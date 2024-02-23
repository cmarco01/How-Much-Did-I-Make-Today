from datetime import date
from re import I
from wsgiref import validate

index = {}

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
    
        
    where = input("\n(OPTIONAL) From what? >> ")
    
    updateIndex(getDate, str(amount), where)



def updateIndex(date, amount, where):
    
    if date in index:
        index[date]["amount"] += ", " + amount
        if where != "":
            index[date]["where"] += ", " + where
        index[date]["num_entries"] += 1
        
        print(index[date]["amount"])
        print(index[date]["where"])
        print(index[date]["num_entries"])
    else:
        index.update({date : {"amount":amount, "where":where, "num_entries":1}})

    init()
        

    
    

init()