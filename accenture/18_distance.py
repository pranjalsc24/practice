import math

def distance(x1,y1,x2,y2,x3,y3):
    first_diff=math.sqrt(math.pow(x2-x1,2)+math.sqrt(math.pow(y2-y1,2)))
    second_diff=math.sqrt(math.pow(x3-x1,2)+math.sqrt(math.pow(y3-y1,2)))
    third_diff=math.sqrt(math.pow(x2-x3,2)+math.sqrt(math.pow(y2-y3,2)))

    print(first_diff,second_diff,third_diff)

distance(1,1,2,4,3,6)    

    