import copy
from Map import *

class DFSAlgorithm:
    def __init__(self, map):
        self.map = map
        self.visited = set()
        self.solution_path = []  # <-- danh sách lưu các bản đồ dẫn đến goal
        # HUY
        self.current_step = 0
        self.auto_play = False
        self.step_delay = 500  # ms
        self.last_step_time = 0

    def search(self, cur_map, path=None):
        if path is None:
            path = []

        cur_signature = tuple(v.position for v in cur_map.vehicles)

        if cur_signature in self.visited:
            return None
        self.visited.add(cur_signature)

        # Thêm map hiện tại vào path
        path.append(cur_map)

        # Kiểm tra goal
        if cur_map.get_goal_cars().position[0] + cur_map.get_goal_cars().vtype == GRID_SIZE:
            self.solution_path = path.copy()  # lưu lại đường đi
            return cur_map

        # Cập nhật domain
        cur_map.get_domain_cars()

        for i, vehicle in enumerate(cur_map.vehicles):
            for new_pos in vehicle.domain:
                if vehicle.position == (new_pos[0], new_pos[1]):
                    continue

                new_map = cur_map.copy()
                new_map.vehicles[i].position = (new_pos[0], new_pos[1])

                result = self.search(new_map, path)
                if result is not None:
                    return result

        path.pop()  # backtrack nếu không đi được
        return None
    
    # BY HUY QUANG TRUONG.
    # bước tiếp theo
    def get_next_step(self):
        if self.current_step < len(self.solution_path) - 1:
            self.current_step += 1
            return self.solution_path[self.current_step]
        return None

    # bước lùi lại 
    def get_previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            return self.solution_path[self.current_step]
        return None

    # tự động chơi
    def toggle_auto_play(self):
        self.auto_play = not self.auto_play
        self.last_step_time = pygame.time.get_ticks()

