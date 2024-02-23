
from datetime import date
from math import e
from os import write
from re import I
from wsgiref import validate
import os

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
    
    if where == "":
        where = "n/a"

    if date in index:
        index[date]["amount"] += ", " + amount
        index[date]["where"] += ", " + where
        index[date]["num_entries"] += 1
        
        print(index[date]["amount"])
        print(index[date]["where"])
        print(index[date]["num_entries"])
    else:
        index.update({date : {"date":date, "amount":amount, "where":where, "num_entries":1}})

    writeToFile(index[date]["date"], index[date]["amount"], index[date]["where"])

    init()
        

def writeToFile(date, amount, where):
    total = getTotal(amount)
    f = open("income_log.txt", "r")    

    if ", " in amount:
        
        temp = open("temp.txt", "a")
        for i in f:
            if date not in i:
                temp.write(i)
        
        f.close()
        newLine = getNewStr(date, amount, where) + str(total) + "\n"
        print(newLine)
        temp.write(newLine)
        temp.close()
        
        temp = open("temp.txt", "r")
        f = open("income_log.txt", "w")    
        # print(temp.read())
        f.write(temp.read())
        temp.close()
        os.remove("temp.txt")
        f.close()
    else:
        f.close()
        f = open("income_log.txt", "a")
        f.write(date + " | $" + amount + " (" + where + ") | TOTAL: $" + str(total) + "\n")
        f.close()
   


def getNewStr(date, amount, where):
    amounts = amount.split(", ")
    wheres = where.split(", ")
    newString = ""
    k = 0
    for i in amounts:
        #print(k)
        if k == len(amounts) - 1:
            newString += "$" + amounts[k] + " (" + wheres[k] + ") | TOTAL: $"
        else: 
            #print(amounts[k] + ", " + wheres[k])
            newString += "$" + amounts[k] + " (" + wheres[k] + ") + "
        k += 1
    
    finalString = date + " | " + newString
    return finalString


def getTotal(amount):
    total = 0
    if ", " in amount:
        # print("multiple amts")
        amounts = amount.split(", ")
        for i in amounts:
            total += int(i)
    else:
        total = int(amount)
        
    # print(str(total))
    return total

init()