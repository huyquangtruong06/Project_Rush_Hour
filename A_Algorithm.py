import time
import tracemalloc
from BinaryMinHeap import BinaryMinHeap
import copy

class A_Algorithm:
    def __init__(self, start_map):
        self.start_map = start_map
        self.solution_path = []
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0
        self.memory_usage_kb = 0

    def search(self, start_map=None):
        if start_map is not None:
            self.start_map = start_map

        start_time = time.time()
        tracemalloc.start()
        heap = BinaryMinHeap()
        heap.push(self.start_map)

        while not heap.is_empty():
            self.max_frontier_size = max(self.max_frontier_size, len(heap.heap))
            current_map = heap.pop()
            self.nodes_expanded += 1

            goal_car = current_map.get_goal_cars()
            if goal_car.position[0] + goal_car.vtype == 6:
                self.solution_path = self.reconstruct_path(current_map)
                self.execution_time = time.time() - start_time
                _, peak = tracemalloc.get_traced_memory()
                self.memory_usage_kb = peak // 1024
                tracemalloc.stop()
                print(f"[A*] Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")
                return current_map

            current_map.get_domain_cars()
            for vehicle in current_map.vehicles:
                for (new_x, new_y, move_cost) in vehicle.domain:
                    new_map = current_map.copy()
                    new_vehicle = next(v for v in new_map.vehicles if v.id == vehicle.id)
                    new_vehicle.position = (new_x, new_y)
                    new_map.cost = current_map.cost - current_map.cal_value_heuristic() + move_cost + new_map.cal_value_heuristic()
                    new_map.parent = current_map
                    if not heap.contains(new_map):
                        heap.push(new_map)

        self.execution_time = time.time() - start_time
        _, peak = tracemalloc.get_traced_memory()
        self.memory_usage_kb = peak // 1024
        tracemalloc.stop()
        print(f"[A*] No solution. Time: {self.execution_time:.4f}s | Nodes expanded: {self.nodes_expanded} | Max frontier size: {self.max_frontier_size} | Memory usage: {self.memory_usage_kb} KB")
        return None

    def reconstruct_path(self, end_map):
        path = []
        current = end_map
        while current:
            path.append(current)
            current = current.parent
        path.reverse()
        return path
