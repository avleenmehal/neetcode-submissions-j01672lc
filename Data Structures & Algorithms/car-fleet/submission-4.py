class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = dict()
        fleets = 0
        for i in range(len(position)):
            time[position[i]] = speed[i]  

        sorted_dict = {k: v for k, v in sorted(time.items())}

        time = []
        # 222111
        # 3 4 5 6 7 8 
        for pos, v in sorted_dict.items():
            # print((target - pos) / v)
            time.append((target - pos) / v)
        
        r = len(time) - 1
        maxtime = time[r]
        while ( r > 0 and time[r] <= maxtime):
            r -=1
            if (time[r]> maxtime):
                fleets += 1
                maxtime = time[r]

        fleets += 1
        
        
        return fleets
        