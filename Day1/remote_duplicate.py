#problem URL:https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List
l1=[]
n=int(input("Enter the number which you want to enter in the list"))

#taking user input 
while(n>0):
    num=int(input())
    l1.append(num)
    n=n-1

class remove_duplicate:
    def __init__(self):
        pass
    
    def remove_dup(self,nums:List[int])->int:
        if not nums:
            return 0

        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k=k+1
        return k
    
obj=remove_duplicate()
print(obj.remove_dup(l1))