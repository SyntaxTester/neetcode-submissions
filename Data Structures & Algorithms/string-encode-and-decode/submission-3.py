class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) != 0:
            
            strs = ' , '.join(strs)
            print(strs)
            return strs

        else:
            strs = 'empty'
            print(strs)
            return strs
            

    def decode(self, s: str) -> List[str]:
        # s = list(s)
        if s != 'empty':
            return s.split(' , ')

        else:
            return []