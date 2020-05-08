#Check If It Is a Straight Line

def straight_line(coordinates):
        val1 = coordinates[0][0]
        val2 = coordinates[0][1]
        flag1,flag2 = True,True
        for i in range(1,len(coordinates)):
            if coordinates[i][0] != val1:
                    flag1 = False
            if coordinates[i][1] != val2:
                    flag2 = False
        if flag1 == True or flag2 == True:
            return True
        flag = True
        val = []
        coordinates.sort(key = lambda x: x[1]) 
        try: 
            for i in range(1,len(coordinates)-1):
                    a =(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
                    b = (coordinates[i+1][0]-coordinates[i-1][0])/(coordinates[i+1][1]-coordinates[i-1][1])
                    val.append(a/b)
            flag = val.count(val[0]) == len(val)   
            return flag
        except:
            return False


coordinates =  [[0,1],[1,3],[-4,-7],[5,11]]
val = straight_line(coordinates)
print(val)     

