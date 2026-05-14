class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {} 
        for i ,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = [] 
            hashmap[num].append(i)  
        for num ,indices in hashmap.items():
            if len(indices) >=2: 
                for i in range(len(indices)-1):
                    if indices[i+1] - indices[i] <=k:
                        return True
        return False