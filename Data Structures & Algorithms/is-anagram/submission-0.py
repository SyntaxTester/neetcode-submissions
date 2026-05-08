class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = False
        s = "".join(sorted(s))
        t = "".join(sorted(t))


        if s == t:
            answer = True

        return answer