#Is a list Palindrome Or Not By Arda Duman.(Long Way)
import time
def reverse(x):
    m=''
    for i in range(len(x)):
        m += x[len(x)-1-i]
        time.sleep(1)
        print(i)
        print(m)
    return m
x=str(input("enter a string : "))
m=reverse(x)
if x == m:
    print("palindrome")
else:
    print("not")
