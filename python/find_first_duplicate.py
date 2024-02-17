class Solution(object):

    def find_first_duplicate(self, array):
        
        # iterate over the array
        for item in array:

            # compare item to next item in array
            for i in range(1, len(array)):
                if array.index(item) != i and item == array[i]:
                    return item

        # return -1 if there are no duplicates    
        return -1

solution = Solution()

print(solution.find_first_duplicate([1,2,4,1,2]))
print(solution.find_first_duplicate([6,2,6]))
print(solution.find_first_duplicate([1,2,3,4,5,6,7,8,9,1]))
print(solution.find_first_duplicate([4,1,5,2]))
print(solution.find_first_duplicate([1]))
print(solution.find_first_duplicate([1,2,3,4,5,6,7,8,9]))