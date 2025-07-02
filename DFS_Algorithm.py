import time
import tracemalloc
import copy
from Map import *

class DFSAlgorithm:
    def __init__(self, map):
        self.map = map
        self.visited = set()
        self.solution_path = []
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0
        self.memory_usage_kb = 0

    def search(self, cur_map, path=None):
        try:
            if path is None:
                path = []

            start_time = time.time()
            tracemalloc.start()
            result = self._dfs(cur_map, path)
            self.execution_time = time.time() - start_time
            _, peak = tracemalloc.get_traced_memory()
            self.memory_usage_kb = peak // 1024
            tracemalloc.stop()

            if result:
                print(f"[DFS] Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")
            else:
                print(f"[DFS] No solution. Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")

            return result
        except RecursionError as e:
            print(f"[DFS] Recursion limit reached: {e}")
            return None

    def _dfs(self, cur_map, path):
        self.max_frontier_size = max(self.max_frontier_size, len(path))
        cur_signature = tuple(v.position for v in cur_map.vehicles)
        if cur_signature in self.visited:
            return None
        self.visited.add(cur_signature)
        self.nodes_expanded += 1

        path.append(cur_map.copy())

        if cur_map.get_goal_cars().position[0] + cur_map.get_goal_cars().vtype == GRID_SIZE:
            self.solution_path = path.copy()
            return cur_map

        cur_map.get_domain_cars()
        for i, vehicle in enumerate(cur_map.vehicles):
            for new_pos in vehicle.domain:
                new_map = cur_map.copy()
                new_map.vehicles[i].position = (new_pos[0], new_pos[1])
                result = self._dfs(new_map.copy(), path)
                if result is not None:
                    return result

        path.pop()
        return None