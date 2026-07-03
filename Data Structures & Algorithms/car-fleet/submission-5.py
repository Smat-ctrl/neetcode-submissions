class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleets = 0
        stack = [] # pair of indices
        res = []
    # position[i] = [1, 2, 3, 4]
    # speed[i] = [20, 30, 40, 50]
    # target = 10 miles
    # speed of car one is 3 miles per hour => 10 - 4 = 6/2 = 3
    # speed of car two is 2 miles per hour => 10 - 1 = 9 / 2 = 4
    # #3 1 mile per hour => 10 - 0 = 10 / 1 = 10
    # #4 1 mile per hour => 10 - 7 = 3 / 1 = 3
        for i in range (len(position)):
            stack.append([position[i], speed[i]])
        stack = sorted(stack)

        while stack:
            position, speed = stack.pop()
            time = (target - position) / speed
            if res:
                if time <= res[len(res) - 1]:
                    continue
            carFleets += 1
            res.append(time)
        return carFleets
