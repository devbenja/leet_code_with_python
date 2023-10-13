# Ejercicio 1: dado un array obtener los 2 indices en los cuales la
# suma de sus valores sea igual a un objetivo dado.

# Hecho el: 12 de octubre del 2023.

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} 
        
        for index, value in enumerate(nums): 
            
            diff = target - value 
                        
            if diff in prevMap: 
                return [prevMap[diff], index] 
            
            prevMap[value] = index   
                    
        return
    
test_solution = Solution()

nums = [2, 7, 11, 15]
target = 9

result = test_solution.two_sum(nums, target)

print(result)