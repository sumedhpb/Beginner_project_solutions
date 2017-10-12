import random

print("Welcome to Dice Rolling Simulator!")
flag=True
while(flag):
    a=int(input("Enter the number of sides your dice should have "))
    b=int(input("Enter the number of times your dice should be rolled "))
    l=[]#list for all possible outcomes when each time the dice is rolled
    ll=[]#unique possible outcomes
    for x in range(b):
        l.append(random.randint(1,a))#gets a random number between l and a(both included)
    for x in l:
        if(x not in ll):
            print(x," occured",l.count(x)," times")
            ll.append(x)
    op=input("Do you want to simulate again? y/n ")
    if(op=="y"):
       flag=True
    else:
       flag=False
    
        
        
        
    
