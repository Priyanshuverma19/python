from turtle import update


myDict = {
    "fast" : " in a quick manner",
    "Harry" : "A coder",
    "Marks" : [1,2,5],
    "anotherdict": {'Harry':'player'}
}
# print(myDict['fast'])
# print(myDict['anotherdict']['harry'])

# Method dictonary
print(myDict.keys())  # print the keys of the dictonary
print(myDict.values()) #-----> print the keys of dictonary
print(myDict.items)     # print the (key,value) for all contents of the dictonary
print(myDict)
updateDict = {
    "Lavish": "friends",
    "Divya": "friends",
    "Harry": "A Dancer"
}
myDict.update(updateDict)   #---> update the dictonry by adding key value pairs from update dict
print(myDict)

print(myDict.get("Harry"))
print(myDict["Harry"])

# print(myDict.get("Harry2"))#  return none as harry2 is not present dict
# print(myDict["Harry2"]) # throw an error as harry2 not present in dict




