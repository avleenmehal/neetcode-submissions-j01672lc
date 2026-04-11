class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedList = []
        for item in strs:
            item = "".join(sorted(item))
            sortedList.append(item)

        mp = defaultdict(list)

        for i in range(len(sortedList)):
            mp[sortedList[i]].append(i)

        print(mp)
        ans = []

        for item in mp:
            arr = []
            for i in mp.get(item):
                arr.append(strs[i])
            ans.append(arr)

        return ans
        