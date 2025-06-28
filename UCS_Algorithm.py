from State import *

class UCSAlgorithm:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.visited = set()
        self.frontiers = [] # Mỗi phần tử là một tuple (cost, state, path)
        self.frontiers.append((0, initial_state, [initial_state]))

    def search(self):
        while self.frontiers:
            cost, current_state, path = self.frontiers.pop(0)

            # Kiểm tra nếu trạng thái đã được thăm
            state_key = current_state.state_to_key()
            if state_key in self.visited:
                continue

            # Đánh dấu trạng thái là đã thăm
            self.visited.add(state_key)

            # Kiểm tra nếu đã đạt đến trạng thái mục tiêu
            if current_state.check_goal():
                return cost, path

            # Sinh ra các trạng thái kế tiếp
            next_states, next_states_cost = current_state.generate_next_states()

            for next_state, next_cost in zip(next_states, next_states_cost):
                new_cost = cost + next_cost
                new_path = path + [next_state]
                self.frontiers.append((new_cost, next_state, new_path))

            # Sắp xếp lại danh sách frontiers theo chi phí (UCS)
            self.frontiers.sort(key=lambda x: x[0])

        return None  # Không tìm thấy đường đi đến trạng thái mục tiêu