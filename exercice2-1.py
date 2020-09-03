def max_of_three(a,b,c):
    maxi = a
    if (a > b) and (a > c):
        maxi = a 
    elif (b > a) and (b > c):
        maxi = b
    else:
        maxi = c

    return maxi

print(max_of_three(1,2,3))