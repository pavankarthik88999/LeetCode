class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth=0
        for i in range(len(accounts)):
            temp=0
            for j in range(len(accounts[i])):
                temp+=accounts[i][j]
            if temp>wealth:
                wealth=temp
        return wealth

        