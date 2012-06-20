'''
creator:obeng william
description:Zellers alogorithm

'''

firstname=raw_input("Enter your first name:")
lastname=raw_input("Enter your last name:")
print "Enter your date of birth"
month=raw_input("       Month as a number betweeen 1-12 ?")
month=int(month)-2

if month <=0:
   month=month+12
   
day=raw_input("         Day?")
year=raw_input("        Year?")
print firstname.upper(),lastname.upper(),"was born on",month,day,year

a=int(month) #month born
b=int(day )#day of month
c=int(year[2:])
d=int(year[:2])

if a==11:
    c=c-1
elif a==12:
    c=c-1
    
w=(13 *a-1)/5
x=c/4
y=d/4
z=w+x+y+b+c-2*d
r=z%7
print "THis is the day in which you were born::",

stop=True
while stop:
    if r <0:
       r=r+7
    if r>0:
        stop=False
        
if r==1:
    print 'monday'
elif r==2:
    print 'tuesday'
elif r==3:
    print 'wednesday'
elif r==4:
    print 'thursday'
elif r==5:
    print 'friday'
elif r==6:
    print 'saturday'
elif r==0:
    print 'sunday'




