class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        # Create position,speed tuple array and sort the array in desecnding order:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for car in cars:
            # If new car is stuck behind the old car, the old car is bottleneck = leader of fleet, don't change anything
            if stk and ((target - car[0]) / car[1] <= (target - stk[-1][0]) / stk[-1][1]):
                continue
            else:
                # create a fleet
                stk.append(car)
        return len(stk)


        
        