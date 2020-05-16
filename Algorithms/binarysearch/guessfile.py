class Sol:
    def guessNumber(self,nums, n):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == n:
                return mid
            elif nums[mid] < n :
                left = mid+1
            else:
                right = mid - 1
        return -1

nums=[-1,0,1,3,4,55,66] 
n=55

a = Sol()
b=a.guessNumber(nums,n)
print(b)