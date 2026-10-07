class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct1={}
        dct2={}
        for i in ransomNote:
            dct1[i]=dct1.get(i,0)+1
        for j in magazine:
            dct2[j]=dct2.get(j,0)+1

        for char,count in dct1.items():
            if dct2.get(char,0)<count:
                return False
            
        return True