from Map import *
class PriorityQueueNode:
    def __init__(self, map_obj):
        self.map = map_obj  # map: đối tượng Map

    def __lt__(self, other):
        return self.map.cost < other.map.cost
    
class BinaryMinHeap:
    def __init__(self):
        self.heap = []
        self.seen_signatures = set()  # lưu chữ ký các trạng thái đã thêm vào

    def push(self, map_obj):
        if self.contains(map_obj):
            return  # bỏ qua nếu map đã tồn tại trong heap

        node = PriorityQueueNode(map_obj)
        self.heap.append(node)
        self.seen_signatures.add(map_obj.get_map_signature())
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        min_node = self.heap.pop()
        self._heapify_down(0)

        sig = min_node.map.get_map_signature()
        self.seen_signatures.discard(sig)  # Xóa khỏi set để cho phép tái chèn nếu cần sau này

        return min_node.map

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def contains(self, map_obj):
        """Kiểm tra xem map đã từng được thêm vào heap chưa"""
        return map_obj.get_map_signature() in self.seen_signatures

    def is_empty(self):
        return len(self.heap) == 0