

target = 7
candidates = [2,3,4,6,7]



def combinationSum(candidates, target):
    index = 0
    for i in range(0,len(candidates)):
        if target >= (candidates[0] + candidates[-1-i]):
            index = i
            break
        
    print(index)






combinationSum(candidates, target)
