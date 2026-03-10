from collections import defaultdict

class Solution:
    def countFrequency(self,arr,n):
        freq_map = defaultdict(int)
        for i in range(n):
            