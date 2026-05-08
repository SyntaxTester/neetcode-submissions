class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem = temperatures
                
        ris = [0] * len(tem)
        k = 0
        count = 0
        for i in range(len(tem)):
            for j in range(len(tem) - 1 - i):
                maxii = tem[i]
                status = 0
                if (maxii >= tem[j + 1 + i - 1 + 1]):
                    k += 1
                    
                elif (maxii < tem[j + 1 + i - 1 + 1]):
                    k += 1
                    count = k
                    break

                        

            ris[i] = count
            k = 0
            count = 0

        
        return ris