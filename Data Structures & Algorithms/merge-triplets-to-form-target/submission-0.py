class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        testing = []
        for triplet in triplets: 
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            testing.append(triplet)
        first = second = third = False

        for triplet in testing: 
            if triplet[0] == target[0]:
                first = True
            if triplet[1] == target[1]:
                second = True 
            if triplet[2] == target[2]:
                third = True
            if first and second and third: 
                return True 
        return False
        

        