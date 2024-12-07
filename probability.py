def aofb(a, b):
    
    if a==1:
        prob = 0.3
        if b==1:
           probdin = 0.75
        else:
            probdin = 0.25
        print("Probability of a given b:", probdin)

    if a==2:
        prob = 0.7
        if b==1:
            probdin = 0.6
        else:
            probdin = 0.4
        print("Probability of a given b:",probdin)

    probaofb = prob*probdin
    return round(probaofb,3)

print("Enter Your Choices")  

print("Is the student freshman? \n 1. Yes \n 2. No")
a = int(input("Enter choice(1/2): "))

print("Is the student eating in dining hall? \n 1. Yes \n 2. No")
b = int(input("Enter choice(1/2): "))

print("Here is the probability:", aofb(a, b))