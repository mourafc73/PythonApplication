def fillBag(**balls):
    global bag
    bag = balls

def totalBalls():
    total = 0
    for color in bag:
        total += bag[color]
    return total
    # alternatively,
    # return sum(bag.values())

def probOf(color):
    return bag[color]/totalBalls()

def probAll():
    probDict = {}
    for color in bag:
        probDict[color] = probOf(color)
    return probDict



testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")



print("totalBalls : ")
try:
    print(testMsg(total == totalBalls()))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probOf")
try:
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False
        
    print(testMsg(passed) )
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probAll")
try:
    print(testMsg(probAll() == prob))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
