REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
TEST_DATA_SMALL = "test_input_data_small.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE
# DATAFILE = TEST_DATA_SMALL


def keep_unique_faces(faces, face):
    for f in faces:
        if face.issubset(f):
            faces.remove(f)
            return
    faces.append(face)


def get_vertex_of_closest_face(faces):
    close_vertex = None
    min_distance = -1
    for face in faces:
        for vertex in face:
            x, y, z = vertex
            distance = x + y + z
            if distance < min_distance or min_distance == -1:
                min_distance = distance
                close_vertex = vertex
    return close_vertex


def get_cube_dots(input_data):
    cube_dots = set()
    for line in input_data:
        x, y, z = list(map(int, line.split(',')))
        cube_dots.add((x, y, z))
    return cube_dots


def get_vertices_and_faces(cube_dot):
    x, y, z = cube_dot
    vertices = {(x, y, z), (x - 1, y, z), (x - 1, y - 1, z), (x - 1, y - 1, z - 1),
                (x - 1, y, z - 1), (x, y - 1, z), (x, y - 1, z - 1), (x, y, z - 1)}
    faces = list()
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if xx == x})
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if xx == x - 1})
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if yy == y})
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if yy == y - 1})
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if zz == z})
    faces.append({(xx, yy, zz) for xx, yy, zz in vertices if zz == z - 1})
    return vertices, faces


def get_min_max_by_cube(cube_dots, cube_dot):
    x, y, z = cube_dot
    min_x = min([xx for xx, yy, zz in cube_dots if yy == y and zz == z])
    max_x = max([xx for xx, yy, zz in cube_dots if yy == y and zz == z])
    min_y = min([yy for xx, yy, zz in cube_dots if xx == x and zz == z])
    max_y = max([yy for xx, yy, zz in cube_dots if xx == x and zz == z])
    min_z = min([zz for xx, yy, zz in cube_dots if xx == x and yy == y])
    max_z = max([zz for xx, yy, zz in cube_dots if xx == x and yy == y])
    return [(min_x, max_x), (min_y, max_y), (min_z, max_z)]


def get_min_max_by_faces(faces):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    for face in faces:
        xs = [x for x, y, z in face]
        ys = [y for x, y, z in face]
        zs = [z for x, y, z in face]
        if min_x == 0 or min(xs) < min_x:
            min_x = min(xs)
        if min_y == 0 or min(ys) < min_y:
            min_y = min(ys)
        if min_z == 0 or min(zs) < min_z:
            min_z = min(zs)
        if max(xs) > max_x:
            max_x = max(xs)
        if max(ys) > max_y:
            max_y = max(ys)
        if max(zs) > max_z:
            max_z = max(zs)
    return [(min_x, max_x), (min_y, max_y), (min_z, max_z)]


def has_no_path_to_exterior(cube_dots, mins_maxs, cube_dot):
    x_range, y_range, z_range = mins_maxs
    xmin, xmax = x_range
    ymin, ymax = y_range
    zmin, zmax = z_range
    already_checked = set()
    to_check = {cube_dot}
    while len(to_check):
        center = to_check.pop()
        already_checked.add(center)
        x, y, z = center
        neighbors = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
        for n in neighbors:
            if n not in already_checked and n not in cube_dots:
                xx, yy, zz = n
                if xmin < xx < xmax and ymin < yy < ymax and zmin < zz < zmax:
                    to_check.add(n)
                else:
                    return False
    return True


def part1(cube_dots):
    all_faces = list()
    for cube_dot in cube_dots:
        x, y, z = cube_dot
        cube_vertices, cube_faces = get_vertices_and_faces(cube_dot)
        for face in cube_faces:
            keep_unique_faces(all_faces, face)
    # print(f'all_faces: {all_faces}')
    return all_faces


def part2(cube_dots, all_faces):
    interior_cubes = set()
    mins_maxs_faces = get_min_max_by_faces(all_faces)
    x_range, y_range, z_range = mins_maxs_faces
    for x in range(x_range[0], x_range[1]+1):
        for y in range(y_range[0], y_range[1]+1):
            for z in range(z_range[0], z_range[1]+1):
                if (x, y, z) not in cube_dots:
                    try:
                        mins_maxs_cube = get_min_max_by_cube(cube_dots, (x, y, z))
                        xx_range, yy_range, zz_range = mins_maxs_cube
                        if xx_range[0] < x < xx_range[1] \
                                and yy_range[0] < y < yy_range[1] \
                                and zz_range[0] < z < zz_range[1] \
                                and has_no_path_to_exterior(cube_dots, mins_maxs_faces, (x, y, z)):
                            interior_cubes.add((x, y, z))
                    except ValueError:
                        continue
    exterior_faces = all_faces.copy()
    for cube_dot in interior_cubes:
        vertices, faces = get_vertices_and_faces(cube_dot)
        for face in faces:
            if face in exterior_faces:
                exterior_faces.remove(face)
    return exterior_faces


def day18(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    cube_dots = get_cube_dots(input_data)
    all_faces = part1(cube_dots)
    print(f'Part1: Face Count: {len(all_faces)}')
    exterior_faces = part2(cube_dots, all_faces)
    print(f'Part2: Face Count: {len(exterior_faces)}')


if __name__ == '__main__':
    day18(DATAFILE)
