#nums = [2,7,11,15]
#target = 9

# nums = [3,2,4]
# target = 6

nums = [3,3]
target = 6

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)






