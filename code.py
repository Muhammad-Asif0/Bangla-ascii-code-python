InputString=input()
count=0
for LoopCounter in range(len(InputString)):
    if ord(InputString[LoopCounter])>=2437 and ord(InputString[LoopCounter])<=2443:
     count=count+1
    elif ord(InputString[LoopCounter])==2447==2448==2482==2524==2525==2510==2527==2528:
      count=count+1
    elif ord(InputString[LoopCounter])>=2451 and ord(InputString[LoopCounter])<=2472:
     count=count+1
    elif ord(InputString[LoopCounter])>=2474 and ord(InputString[LoopCounter])<=2480:
     count=count+1
    elif ord(InputString[LoopCounter])>=2486 and ord(InputString[LoopCounter])<=2489:
     count=count+1
    elif ord(InputString[LoopCounter])>=2492 and ord(InputString[LoopCounter])<=2500:
     count=count+1

if count>0:
    print("It is a bangla line")
else:
    print("It is not a bangla line")

    
    
