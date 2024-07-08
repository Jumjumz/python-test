print("Try programiz.pro")

val = []

print (type (val))
print(type (type (val)))

sets = {"dead", "alive", "barely"}

sets.remove("barely")
sets.add("walking")
sets.remove("dead")
sets.remove("walking")
sets.add("dead")
sets.add("barely")
print (type (sets))

print(sets)

users = {1: {"fname": "Jummer", "lname": "Ramos", "Age": 26}, 2: {"fname": "Gianna", "lname": "Ramos", "Age": [10, 20, 30], "Days": (10, 20, 30), "Teeth": {1: 20, 2: 30, 4: [60, 70, 80], 5: (100, 200, 300, "ssss")}} }
print("\nFirstname: {}\nLastname: {}\nAge: {}".format(users[1]["fname"], users[1]["lname"], users[1]["Age"]))
print(type(users[1]))
print(users[2]["Age"][0])
print(users[2]["Days"][1])
print(users[2]["Teeth"][4][1])
print(type(users[2]["Teeth"][4][1]))
print(type(users[2]["Teeth"][5]))

if(type (users[1]) == type (users[2])):
    print("Both types are the same")
    print(type (users[1]), "equal", type (users[2]))
else :
    print("Not equal")
    
if (type (users[1]) and type (users[2]) == type (users[1])):
    print("int")