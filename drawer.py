import AnkitDraw

exit = False
#/usr/bin/env python3

# A SIMPLE DRAWING PROGRAM WRITTEN IN PYTHON


while( not exit):
 print("AnkitVIEW")
 print("1. CIRCLE")
 print("2. POLYGON")
 print("3. LINE")
 print("4. RECTANGLE")
 print("5 .ANGLED LINE")
 print("6.EXIT")
 choice = int(input('Choice:'))
 
 if(choice == 1):
    l = int(input('Radius: '))
    AnkitDraw.circle(l)

 elif(choice == 2):
    n = int(input('Side Count: '))
    l = int(input('Side Length: '))
    AnkitDraw.polygon(n,l)

 elif(choice == 3):
    l = int(input('Length: '))
    angle = int(input('Angle: '))
    AnkitDraw.line(l,angle)

 elif(choice == 4):
   l = int(input('Length: '))
   b = int(input('Breadth: '))
   AnkitDraw.rect(l,b)
 
 elif(choice == 5):
    l = int(input('Length: '))
    angle = int(input('Angle: '))
    AnkitDraw.aLine(l,angle)

 elif(choice == 6):
     exit = True

 else:
     print("Invalid Choice!!!")    


#WRITTEN BY ANKIT DAS on 1st April 2020
