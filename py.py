import time
x = int(input("enter a number = "))
y = range(1,x)
z = []
for m in y:
    time.sleep(0.3)
    print("trying to add more")
    if x%m==0:
        print (m)
        z.append(m)
    else:
        pass
    print(z)
