def Roll(face,num):
    aa = [x+1 for x in range(face)]
    if num == 1:
        return aa
    if num > 1:
        return (x+y for x in aa for y in Roll(face,num-1))

def chance(face,num):
    aa = Roll(face,num)
    probability = {}
    for i in aa:
        if i in probability:
            probability[i] += 1
        else:
            probability[i] = 1
    print(probability)
    total = sum(probability.values())        
    for i in probability:
        print("The probability of %d is %f" % (i,probability[i]/total))
       
chance(6,3)
