from BinaryMinHeap import BinaryMinHeap  # import cây nhị phân đã viết
import copy

class UCSAlgorithm:
    def __init__(self, start_map):
        self.start_map = start_map

    def search(self):
        heap = BinaryMinHeap()
        heap.push(self.start_map)

        while not heap.is_empty():
            current_map = heap.pop()

            goal_car = current_map.get_goal_cars()
            if goal_car.position[0] + goal_car.vtype == 6:
                return current_map  # Trạng thái đích đã đạt

            current_map.get_domain_cars()

            for vehicle in current_map.vehicles:
                for (new_x, new_y, move_cost) in vehicle.domain:
                    # Tạo bản sao map và di chuyển vehicle
                    new_map = current_map.copy()
                    new_vehicle = next(v for v in new_map.vehicles if v.id == vehicle.id) #find vehicle by id
                    new_vehicle.position = (new_x, new_y)

                    # Cập nhật thông tin map mới
                    new_map.cost = current_map.cost + move_cost
                    new_map.parent = current_map

                    # Thêm vào heap nếu chưa tồn tại
                    if not heap.contains(new_map):
                        heap.push(new_map)
                    

        return None  # Không tìm thấy lời giải
