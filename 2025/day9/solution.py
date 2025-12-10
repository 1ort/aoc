
red_tiles = []
with open('input.txt') as f:
    for line in f:
        red_tiles.append(tuple(map(int, line.split(','))))

# def is_any_tile_in_rectangle(x1, y1, x2, y2) -> bool:
#     for tile_x, tile_y in red_tiles:
#         if (
#             (x1 < tile_x < x2 or x1 > tile_x > x2)
#             and 
#             (y1 < tile_y < y2 or y1 > tile_y > y2)
#         ):
#             return True
#     return False


max_area = 0

for i, (x1, y1) in enumerate(red_tiles):
    for (x2, y2) in red_tiles[i+1:]:
        area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
        if area > max_area:
            max_area = area

print('pt1:', max_area)

