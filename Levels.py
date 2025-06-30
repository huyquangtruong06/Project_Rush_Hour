from Vehicles import Vehicle, Orientations, VehicleTypes

vehicles_map = [
    # Map 1: Dễ (3 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),  # Xe cần thoát
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (0, 3), Orientations.vertical, VehicleTypes.car, 2),
    ],

    # Map 2: Dễ vừa (4 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (1, 0), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (4, 1), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 4), Orientations.horizontal, VehicleTypes.car, 3),
    ],

    # Map 3: Trung bình (5 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (1, 3), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 0), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (4, 4), Orientations.vertical, VehicleTypes.car, 4),
    ],

    # Map 4: Trung bình-khá (6 xe)
    [
        Vehicle("A", (1, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (0, 4), Orientations.horizontal, VehicleTypes.car, 2),
        Vehicle("D", (3, 1), Orientations.vertical, VehicleTypes.truck, 3),
        Vehicle("E", (4, 3), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (5, 0), Orientations.vertical, VehicleTypes.car, 5),
    ],

    # Map 5: Khó (7 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (1, 1), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (3, 0), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (4, 2), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (5, 3), Orientations.horizontal, VehicleTypes.car, 5),
        Vehicle("G", (0, 5), Orientations.horizontal, VehicleTypes.car, 6),
    ],

    # Map 6: Khó hơn (7 xe với nhiều chướng ngại)
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (2, 3), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (3, 0), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 2), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (3, 4), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (5, 4), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (4, 3), Orientations.horizontal, VehicleTypes.car, 6),
    ],

    # Map 7: Rối rắm (8 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (0, 3), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (1, 1), Orientations.vertical, VehicleTypes.truck, 3),
        Vehicle("E", (3, 0), Orientations.vertical, VehicleTypes.car, 4),
        Vehicle("F", (4, 2), Orientations.horizontal, VehicleTypes.truck, 5),
        Vehicle("G", (5, 4), Orientations.vertical, VehicleTypes.car, 6),
        Vehicle("H", (2, 5), Orientations.horizontal, VehicleTypes.car, 7),
    ],

    # Map 8: Khó cấp độ cao (8 xe phức tạp)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (1, 1), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (3, 0), Orientations.vertical, VehicleTypes.truck, 3),
        Vehicle("E", (4, 1), Orientations.horizontal, VehicleTypes.truck, 4),
        Vehicle("F", (0, 4), Orientations.vertical, VehicleTypes.truck, 5),
        Vehicle("G", (2, 5), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (5, 3), Orientations.vertical, VehicleTypes.truck, 7),
    ],

    # Map 9: Cực khó (9 xe)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (0, 3), Orientations.vertical, VehicleTypes.truck, 2),
        Vehicle("D", (1, 1), Orientations.horizontal, VehicleTypes.truck, 3),
        Vehicle("E", (3, 0), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (4, 1), Orientations.horizontal, VehicleTypes.truck, 5),
        Vehicle("G", (1, 4), Orientations.vertical, VehicleTypes.truck, 6),
        Vehicle("H", (3, 4), Orientations.horizontal, VehicleTypes.car, 7),
        Vehicle("I", (5, 5), Orientations.horizontal, VehicleTypes.truck, 8),
    ],

    # Map 10: Siêu khó (10 xe với nhiều bẫy)
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (0, 3), Orientations.vertical, VehicleTypes.truck, 2),
        Vehicle("D", (1, 1), Orientations.horizontal, VehicleTypes.truck, 3),
        Vehicle("E", (3, 0), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (4, 1), Orientations.horizontal, VehicleTypes.truck, 5),
        Vehicle("G", (1, 4), Orientations.vertical, VehicleTypes.truck, 6),
        Vehicle("H", (3, 3), Orientations.vertical, VehicleTypes.truck, 7),
        Vehicle("I", (5, 0), Orientations.horizontal, VehicleTypes.truck, 8),
        Vehicle("J", (5, 4), Orientations.vertical, VehicleTypes.truck, 9),
    ],
]