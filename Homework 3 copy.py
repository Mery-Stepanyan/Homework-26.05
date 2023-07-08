nestedList = [[0,'M',0,'M',0], [0,0,'M',0,0],[0,0,0,0,0], ['M','M',0,0,0], [0,0,0,'M',0]]

print(nestedList)


for i in range(0,len(nestedList)) : 
   M_sum=0
   for j in range(0,len(nestedList)) : 
        if nestedList[i][j]=="M":
            pass
        elif nestedList[i][j]==0:
            if (i-1)==-1 or (j-1)==-1:
                continue
                if nestedList[i-1][j-1]=="M":
                    M_sum+=1
                    if nestedList[i-1][j]=="M":
                        M_sum+=1
                        if nestedList[i-1][j+1]=="M":
                            M_sum+=1
                       
                            if nestedList[i][j-1]=="M":
                                M_sum+=1
                                if nestedList[i][j+1]=="M":
                                    M_sum+=1
                             
                             
                                    if nestedList[i+1][j-1]=="M":
                                        M_sum+=1
                                        if nestedList[i+1][j]=="M":
                                            M_sum+=1
                                            if nestedList[i+1][j+1]=="M":
                                               M_sum+=1
        nestedList[i][j]=M_sum

        print(nestedList[i][j]) 

        