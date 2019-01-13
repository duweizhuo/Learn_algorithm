aa = list(range(1,7))
def Roll(face_num, dice_num):
    all = []
    face_list = list(range(1,face_num+1))
    if dice_num == 1:
        return face_list
    elif dice_num > 1:
        bb = [x+y for x in aa for y in Roll(face_num, dice_num-1)]
        return bb
    
    

def count1(face_num, dice_num):
    
    all_Num = Roll(face_num, dice_num)
    All = {}
    for i in all_Num:
        if i in All:
            All[i] += 1
        else:
            All[i] = 1
#    return All

    all_chance = sum(All.values())
    for i in All:
       print("The probability of %d is %f" %(i,All[i]/all_chance))
      
print(count1(6,4))
