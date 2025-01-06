
List1 = [1,2,4] 
List2 = [1,3,4] 


def removeDuplicates(List1, List2):
    final = []
    
    i = 0
    ii = 0

    while len(final) < (len(List1) + len(List2)):
        batch = []

        if (List1[i]) and (List2[ii]):
            if (List1[i] < List2[ii]):
                batch.append(List1[i]) 
            
            while List2[ii] < List1[i]:
                print(List2[ii])
                ii+=1
       

        print(List1[i])
        i+=1




removeDuplicates(List1, List2)



