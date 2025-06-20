class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        max_num = 5000

        for i in range(max_num):
            cnt = 0
            for citation in citations:
                if citation >= i:
                    cnt +=1
            if cnt == 0:
                break
            elif cnt >= i:
                h_index = i

        return h_index 
            
