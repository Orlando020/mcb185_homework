def meltoligo(a, c, g, t):
    if a+c+g+t <= 13: 
        return (a+t)*2+(g+c)*2
    else:
        return 64.9 + 41*(g+c-16.4)/(a+c+g+t)
        
print(meltoligo(41,51,224,63))
print(meltoligo(0,2,1,4))
print(meltoligo(4141,5345,6263,2373))
print(meltoligo(5,7,3,4))