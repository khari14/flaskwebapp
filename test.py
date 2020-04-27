def array_madness(a,b):
    if sum(list(map(lambda num: num**2, a))) > sum(list(map(lambda num: num**2, b))):
        print (True)
    else:
        print (False)

array_madness([4,2],[3])

