
class Solution: 
    def reconstructionQueue(self, input):
        input.sort(key = lambda x : (-x[0], x[1]))
    
        res = []
        for person in input:
            res.insert(person[1], person)
        return res

input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructionQueue(input))
#[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]