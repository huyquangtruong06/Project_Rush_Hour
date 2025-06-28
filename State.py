from Map import Map
from Vehicles import *

class State:
    def __init__(self, vehicles):
        """Initialize the state with a list of vehicles."""
        self.vehicles = vehicles
        self.next_states = []
        self.next_states_cost = []

    def generate_vehicle_grid(self, vehicles):
        # Khởi tạo mảng 2 chiều kích thước grid_size x grid_size toàn là "0"
        grid = [["0" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # Duyệt từng xe trong danh sách
        for vehicle in vehicles:
            for position in vehicle.coveredUnits():
                x, y = position
                if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    grid[y][x] = vehicle.id  # Lưu ý: y là hàng, x là cột (tọa độ theo màn hình)
        
        return grid

    def generate_next_states(self):
        """
        Sinh ra tất cả các trạng thái kế tiếp có thể từ trạng thái hiện tại.
        Mỗi trạng thái tạo ra bằng cách di chuyển một xe hợp lệ một bước.
        """
        next_states = []
        next_states_cost = []

        current_grid = self.generate_vehicle_grid(self.vehicles) # Tạo bản đồ xe hiện tại

        for i, vehicle in enumerate(self.vehicles): # Duyệt qua từng xe
            # Xác định hướng di chuyển của xe
            dx = int(vehicle.orientation == Orientations.horizontal)
            dy = int(vehicle.orientation == Orientations.vertical)

            for direction in [-1, 1]:  # Thử cả hai hướng: lùi và tiến
                # Tính vị trí mới nếu di chuyển 1 bước theo hướng đó
                new_head_x = vehicle.position[0] + dx * direction
                new_head_y = vehicle.position[1] + dy * direction
                new_tail_x = vehicle.position[0] + dx * (int(vehicle.vtype) - 1) + dx * direction
                new_tail_y = vehicle.position[1] + dy * (int(vehicle.vtype) - 1) + dy * direction

                # Kiểm tra vị trí đầu/tail mới có nằm trong bản đồ không
                if not (0 <= new_head_x < GRID_SIZE and 0 <= new_head_y < GRID_SIZE and
                        0 <= new_tail_x < GRID_SIZE and 0 <= new_tail_y < GRID_SIZE):
                    continue

                # Kiểm tra xem vị trí mới có bị chiếm bởi xe khác không
                if direction == -1:
                    check_x = vehicle.position[0] - dx
                    check_y = vehicle.position[1] - dy
                else:
                    check_x = vehicle.position[0] + dx * int(vehicle.vtype)
                    check_y = vehicle.position[1] + dy * int(vehicle.vtype)

                if not (0 <= check_x < GRID_SIZE and 0 <= check_y < GRID_SIZE):
                    continue

                if current_grid[check_y][check_x] == "0":
                    # Tạo bản sao state mới
                    new_vehicles = [v.copy() for v in self.vehicles]
                    new_vehicles[i].position = (new_head_x, new_head_y)
                    new_state = State(new_vehicles)
                    next_states.append(new_state)
                    next_states_cost.append(vehicle.vtype)  # Chi phí di chuyển là kích thước xe

        return next_states, next_states_cost
    
    def state_to_key(self):
        """Chuyển state thành khóa duy nhất (định danh)."""
        return tuple((v.id, v.position, v.orientation) for v in self.vehicles)
    
    def check_goal(self):
        """Kiểm tra xem trạng thái hiện tại có phải là trạng thái mục tiêu không."""
        target_vehicle = next((v for v in self.vehicles if v.id == "A"), None)
        y = target_vehicle.position[1]

        return target_vehicle.position == (GRID_SIZE - 2, y)

    



