class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        if nums == []:
            return 0
        for num in nums:
            if num not in hashmap: hashmap[num] = 1
            else: hashmap[num]+=1
        
        starts = []
        for key in hashmap.keys():
            if key-1 not in hashmap:
                starts.append(key)
        
        mx = 1
        for start in starts:
            k = start+1
            l = 1
            while k in hashmap:
                l+=1
                k+=1
            
            mx = max(l,mx)
        
        return mx
                

        