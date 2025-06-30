from Vehicles import Vehicle, Orientations, VehicleTypes

vehicles_map = [
    # Map 1: 
    [
        Vehicle("A", (2, 2), Orientations.horizontal, VehicleTypes.car, 0),  # Xe cần thoát
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (0, 3), Orientations.vertical, VehicleTypes.car, 2),
    ],

    # Map 2:
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (1, 1), Orientations.horizontal, VehicleTypes.car, 1),
        Vehicle("C", (2, 3), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 1), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (3, 2), Orientations.vertical, VehicleTypes.car, 4),
        Vehicle("F", (3, 5), Orientations.horizontal, VehicleTypes.car, 5),
    ],

    # Map 3: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 3), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (1, 5), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (2, 0), Orientations.horizontal, VehicleTypes.truck, 3),
        Vehicle("E", (2, 2), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (3, 1), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (3, 3), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (4, 4), Orientations.vertical, VehicleTypes.car, 7),
    ],

    # Map 4: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (2, 3), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (3, 0), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 2), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (3, 4), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (5, 4), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (4, 3), Orientations.horizontal, VehicleTypes.car, 6),
    ],

    # Map 5: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 5), Orientations.horizontal, VehicleTypes.car, 1),
        Vehicle("C", (1, 0), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (2, 3), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (3, 1), Orientations.vertical, VehicleTypes.car, 4),
        Vehicle("F", (3, 3), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (4, 0), Orientations.vertical, VehicleTypes.truck, 6),
        Vehicle("H", (4, 3), Orientations.horizontal, VehicleTypes.car, 7),
        Vehicle("I", (4, 5), Orientations.horizontal, VehicleTypes.car, 8),
        Vehicle("J", (5, 0), Orientations.vertical, VehicleTypes.truck, 9),
    ],

    # Map 6: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (1, 1), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (2, 0), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (4, 0), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (1, 3), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (2, 3), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (2, 4), Orientations.vertical, VehicleTypes.car, 7),
        Vehicle("I", (3, 4), Orientations.horizontal, VehicleTypes.car, 8),
        Vehicle("J", (5, 2), Orientations.vertical, VehicleTypes.truck, 9),
    ],

    # Map 7: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 5), Orientations.horizontal, VehicleTypes.car, 1),
        Vehicle("C", (1, 3), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (2, 0), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (2, 1), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (2, 4), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (3, 5), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (4, 0), Orientations.vertical, VehicleTypes.truck, 7),
        Vehicle("I", (4, 4), Orientations.horizontal, VehicleTypes.car, 8),
        Vehicle("J", (5, 1), Orientations.vertical, VehicleTypes.truck, 9),
    ],

    # Map 8: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 3), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (2, 0), Orientations.vertical, VehicleTypes.truck, 2),
        Vehicle("D", (1, 3), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (3, 1), Orientations.vertical, VehicleTypes.truck, 4),
        Vehicle("F", (4, 0), Orientations.horizontal, VehicleTypes.car, 5),
        Vehicle("G", (4, 1), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (4, 3), Orientations.horizontal, VehicleTypes.car, 7),
        Vehicle("I", (3, 5), Orientations.horizontal, VehicleTypes.car, 8),
        Vehicle("J", (5, 4), Orientations.vertical, VehicleTypes.car, 9),
    ],

    # Map 9: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 0), Orientations.vertical, VehicleTypes.car, 1),
        Vehicle("C", (0, 4), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (1, 1), Orientations.horizontal, VehicleTypes.car, 3),
        Vehicle("E", (1, 5), Orientations.horizontal, VehicleTypes.truck, 4),
        Vehicle("F", (2, 3), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (3, 0), Orientations.vertical, VehicleTypes.car, 6),
        Vehicle("H", (3, 3), Orientations.vertical, VehicleTypes.car, 7),
        Vehicle("I", (4, 2), Orientations.vertical, VehicleTypes.car, 8),
        Vehicle("J", (4, 4), Orientations.horizontal, VehicleTypes.car, 9),
        Vehicle("K", (4, 5), Orientations.horizontal, VehicleTypes.car, 10),
        Vehicle("L", (5, 1), Orientations.vertical, VehicleTypes.truck, 11),
    ],
    # Map 10: 
    [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (0, 3), Orientations.horizontal, VehicleTypes.truck, 1),
        Vehicle("C", (1, 1), Orientations.horizontal, VehicleTypes.car, 2),
        Vehicle("D", (1, 4), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (2, 4), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (3, 5), Orientations.horizontal, VehicleTypes.truck, 5),
        Vehicle("G", (4, 0), Orientations.horizontal, VehicleTypes.car, 6),
        Vehicle("H", (4, 1), Orientations.vertical, VehicleTypes.truck, 7),
        Vehicle("I", (5, 1), Orientations.vertical, VehicleTypes.car, 8),
    ],
]