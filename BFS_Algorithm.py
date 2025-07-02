import time
import tracemalloc
from collections import deque
import copy
from Map import *

class BFSAlgorithm:
    def __init__(self, map):
        self.map = map
        self.visited = set()
        self.solution_path = []
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0
        self.memory_usage_kb = 0

    def search(self, start_map):
        start_time = time.time()
        tracemalloc.start()

        queue = deque()
        queue.append((start_map.copy(), []))

        while queue:
            self.max_frontier_size = max(self.max_frontier_size, len(queue))
            current_map, path = queue.popleft()
            signature = tuple(v.position for v in current_map.vehicles)

            if signature in self.visited:
                continue
            self.visited.add(signature)
            self.nodes_expanded += 1

            path = path + [current_map]

            goal_car = current_map.get_goal_cars()
            if goal_car.position[0] + goal_car.vtype == GRID_SIZE:
                self.solution_path = path
                self.execution_time = time.time() - start_time
                _, peak = tracemalloc.get_traced_memory()
                self.memory_usage_kb = peak // 1024
                tracemalloc.stop()
                print(f"[BFS] Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")
                return current_map

            current_map.get_domain_cars()
            for i, vehicle in enumerate(current_map.vehicles):
                for new_pos in vehicle.domain:
                    if vehicle.position == new_pos:
                        continue
                    new_map = current_map.copy()
                    new_map.vehicles[i].position = new_pos
                    queue.append((new_map, path))

        self.execution_time = time.time() - start_time
        _, peak = tracemalloc.get_traced_memory()
        self.memory_usage_kb = peak // 1024
        tracemalloc.stop()
        print(f"[BFS] No solution. Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")
        return None
