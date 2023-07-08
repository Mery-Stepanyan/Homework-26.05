# Task 2 Write a program that rotates a matrix by 180 degrees.

our_list=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in our_list:
    print (i)
our_list.reverse()
reversed_list=[]    
for i in range(len(our_list)):
    newlist=our_list[i]
    newlist.reverse()
    reversed_list.append(newlist)
print("********Reversed list******")    
for i in reversed_list:
    print(i)
   
# Task 3 Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate. An example is shown below.    

hour=int(input("Please enter an hour  between 1 and 12: "))
if hour>12 or hour<1:
    print("Try again, your entered number is wrong")
else:
    message_am_pm=input("Please enter 1 for AM and 2 FOR PM: ")
    hours_ahead=int(input("How many hours into the future you do want to go: "))
    while(hours_ahead>24):
        hours_ahead=hours_ahead-24
        
    if(message_am_pm=="AM"):
        new_hour=hour+hours_ahead
        if(new_hour==24):
            print("New hour: "+str(new_hour-12)+" "+"AM")
        if(new_hour<12):
            print("New hour: "+str(new_hour)+" "+message_am_pm)
        if(new_hour<24 and new_hour>12):
            print("New hour: "+str(new_hour-12)+" "+"PM")
        if(new_hour==12):
            print("New hour: "+str(new_hour)+" "+"PM")
        if(new_hour>24):
            print("New hour: "+str(new_hour-24)+" "+"AM")
            
    if(message_am_pm=="PM"):
        new_hour=hour+hours_ahead
        if(new_hour==24):
            print("New hour: "+str(new_hour-12)+" "+"PM")
        if(new_hour<12):
            print("New hour: "+str(new_hour)+" "+message_am_pm)
        if(new_hour<24 and new_hour>12):
            print("New hour: "+str(new_hour-12)+" "+"AM")
        if(new_hour==12):
            print("New hour: "+str(new_hour)+" "+"AM")
        if(new_hour>24):
            print("New hour: "+str(new_hour-24)+" "+"PM")        
    