#Ben Glaspie
#This is my code it will make a yellow and red star 
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
''' now I will ask what they thought about my code 
using a simple print code '''

rate_out_of_10 = (input("Rate my star out of 10: "))
thankyou = (input("Thank you for rateing my star!"))

print(rate_out_of_10)
print(thankyou)


#This was what I did so I could pull my code when I got to school
