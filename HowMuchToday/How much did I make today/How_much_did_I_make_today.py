
from datetime import date
from math import e
from os import write
from re import I
from wsgiref import validate
import os
import json
import keyboard

try:
    with open('data.json', 'r') as openfile:
        # Reading from json file
        # Loads json file (if it exists), which is basically just
        # loading the dictionary
        json_object = json.load(openfile)
except:
    # if there is no json file, create it and put an empty dictionary in there
    with open('data.json', 'w') as openfile:
        json.dump({}, openfile)
    with open('data.json', 'r') as openfile:
        # Reading from json file
        # Then get what is just a blank dictionary
        json_object = json.load(openfile)
        

# Set our index to the json object (dictionary). This is basically just
# loading from a save
index = json_object
# print(index)


def init():
    today = date.today()
    getDate = today.strftime("%B %d, %Y")
    # print(getDate)

    validAmount = False
   
    while validAmount == False:
        try:
            amount = float(input("\nWhat's goood, me!! How much did we make today?? (" + getDate + ") >>  "))
        except ValueError:
            print("\n\tThat's not a number, fool! Try again.")
            continue
        else:
            amount = round(amount)
            print("\n\tWe gooood, rounding to nearest dollar: $" + str(amount))
            validAmount = True
            break
    
        
    where = input("\n(OPTIONAL) From what? >> ")
    
    updateIndex(getDate, str(amount), where)



def updateIndex(date, amount, where):
    # print(index)    

    if where == "":
        where = "n/a"

    # if the date doesn't exist, add a new entry w/ that date
    # if the date does exist, update the entry at that date
    if date in index:
        index[date]["amount"] += ", " + amount
        index[date]["where"] += ", " + where
        index[date]["num_entries"] += 1
        
        #print(index[date]["amount"])
        #print(index[date]["where"])
        #print(index[date]["num_entries"])
    else:
        index.update({date : {"date":date, "amount":amount, "where":where, "num_entries":1}})
    

    # our index is fully up to date, so let's set a json object
    # to our dictionary, which is done w/ the following
    json_obj = json.dumps(index, indent=4)
    
    # then, overwrite our whole data.json file w/ the correct,
    # up-to-date index. so now our index and json objects are the same
    # and up to date
    with open("data.json", "w") as outfile:
        outfile.write(json_obj)

    # print(index)
    
    writeToFile(index[date]["date"], index[date]["amount"], index[date]["where"])

    
    init()
    
        

def writeToFile(date, amount, where):
    total = getTotal(amount)
    
    # this signifies that the entry for the date has been updated
    # more than once in the same day; therefore we know that date
    # exists and can update the log file accordingly
    if ", " in amount:
        # print("\t\t\nDATE IN LOG FILE")
        f = open("income_log.txt", "r")   
        temp = open("temp.txt", "a")
        for i in f:
            if date not in i:
                temp.write(i)
        
        f.close()
        newLine = getNewStr(date, amount, where) + str(total) + "\n"
        # print(newLine)
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