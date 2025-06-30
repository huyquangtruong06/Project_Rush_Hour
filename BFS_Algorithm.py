import copy
from collections import deque
from Map import *

class BFSAlgorithm:
    def __init__(self, map):
        self.map = map
        self.visited = set()
        self.solution_path = []

    def search(self, start_map):
        queue = deque()
        queue.append((start_map.copy(), []))  # (current_map, path_to_current)

        while queue:
            current_map, path = queue.popleft()
            signature = tuple(v.position for v in current_map.vehicles)

            if signature in self.visited:
                continue
            self.visited.add(signature)

            # Append current state to path
            path = path + [current_map]

            # Check if current state is goal
            goal_car = current_map.get_goal_cars()
            if goal_car.position[0] + goal_car.vtype == GRID_SIZE:
                self.solution_path = path
                return current_map

            # Expand possible moves
            current_map.get_domain_cars()
            for i, vehicle in enumerate(current_map.vehicles):
                for new_pos in vehicle.domain:
                    if vehicle.position == new_pos:
                        continue

                    new_map = current_map.copy()
                    new_map.vehicles[i].position = new_pos
                    queue.append((new_map, path))

        # If no solution
        return None




    
    

