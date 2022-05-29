# Question: https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list, speed: list) -> int:
        # Time taken for a car to reach target
        times = []

        # Positions in reverse order cuz 
        # times should reduce if all the cars go in same speed
        for p, s in reversed(sorted(zip(position, speed))):

            # finding distance
            distance = target-p

            # if the existing time is less than given time, 
            # at some point of journey, they will meet and form a fleet
            # if the time taken is greater than what is already present,
            # then they will not meet till destination, so we add to times list
            if (not times) or ((distance/s)>times[-1]):
                times.append((distance/s))
        
        # Different times represent different fleets of cars
        return len(times)