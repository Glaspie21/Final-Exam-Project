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
They will rate it out of 10'''

rate_out_of_10 = (input("Rate my star out of 10: "))
thankyou = (input("Thank you for rateing my star!"))

print(rate_out_of_10)
print(thankyou)
