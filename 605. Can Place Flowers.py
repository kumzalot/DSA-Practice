class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb = [0] + flowerbed + [0] #to tackle edgecases

        for i in range(1, len(fb) - 1): #iterating thru flowerbed arr only
            if fb[i] == 0 and fb[i-1] == 0 and fb[i+1] == 0:
                fb[i] = 1
                n -= 1
        
        if n<=0:
            return True
        else:
            return False

