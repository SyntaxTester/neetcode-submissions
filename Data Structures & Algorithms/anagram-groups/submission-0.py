class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = strs.copy()


        for i in range(len(strs)):
            lst[i] = ''.join(sorted(lst[i])) # делаем слова одинаковыми 

        filtered = list(dict.fromkeys(lst)) # убираем дубликаты, чтобы сверять
        superlist = [[] for _ in range(len(filtered))] # сюда анаграммы

        for i in range(len(filtered)):
            for j in range(len(lst)):
                if lst[j] == filtered[i]:
                    superlist[i].append(strs[j])
            
        
        return superlist