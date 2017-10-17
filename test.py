import json

fileName = 'd:\\python\\name.json'

try:
    with open(fileName) as fileObj:
        userName = json.load(fileObj)
except FileNotFoundError:
    userName = input("what's your name:")
    with open(fileName, 'w') as fileObj:
        json.dump(userName, fileObj)
        print("Welcome, " + userName)
else:
    print("Welcome back, " + userName)
