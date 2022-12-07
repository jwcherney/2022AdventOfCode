REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


class File:
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return "F: " + self.parent.get_path() + self.name + ": " + str(self.get_size())


class Directory:
    def __init__(self, parent, name, contents):
        self.parent = parent
        self.name = name
        if not self.name.endswith('/'):
            self.name += '/'
        self.contents = contents

    def get_size(self):
        total = 0
        for item in self.contents:
            total += item.get_size()
        return total

    def get_all_dirs_sizes(self):
        return_value = [self.get_size()]
        for x in self.contents:
            if type(x) is Directory:
                return_value.extend(x.get_all_dirs_sizes())
        return return_value

    def append(self, item):
        self.contents.append(item)

    def get_by_name(self, name):
        if not name.endswith('/'):
            name += '/'
        for item in self.contents:
            if item.name == name:
                return item
        return None

    def get_path(self):
        path = ''
        if self.parent is not None:
            path = self.parent.get_path()
        path += self.name
        return path

    def __str__(self):
        return "D: " + self.get_path() + ": " + str(self.get_size())


def parse_input(input_lines):
    top_directory = None
    current_directory = None
    for line in input_lines:
        # print(f'line: {line}')
        if line == '':
            continue
        words = line.split()
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    current_directory = current_directory.parent
                else:
                    if words[2] == '/':
                        top_directory = Directory(None, words[2], [])
                        current_directory = top_directory
                    else:
                        current_directory = current_directory.get_by_name(words[2])
                        if current_directory is None:
                            print(f"Error: {words[2]} not found")
            elif words[1] == "ls":
                continue
            else:
                # print(f'Unknown Command: {words[1]}')
                return None
        elif words[0] == "dir":
            d = Directory(current_directory, words[1], [])
            current_directory.append(d)
            # print(f'Found directory: {d}')
        else:
            f = File(current_directory, words[1], int(words[0]))
            # print(f'Found file: {f}')
            current_directory.append(f)
        # print(f'current_directory: {current_directory}')
    return top_directory


def day07(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    file_structure = parse_input(input_data)
    # print(f'File Structure: {file_structure}')
    dirs = file_structure.get_all_dirs_sizes()
    # print(f'Dirs : {dirs}')
    dirs_hundredk = [x for x in dirs if x <= 100000]
    # print(f'Dirs hundredk: {dirs_hundredk}')
    print(f'Part 1: Total of 100k dirs: {sum(dirs_hundredk)}')
    dirs.sort(reverse=True)
    unused_space = 70000000 - file_structure.get_size()
    # print(f'Unused Space: {unused_space}')
    space_needed = 30000000 - unused_space
    # print(f'Space needed: {space_needed}')
    dirs_8m = [x for x in dirs if x >= space_needed]
    print(f'Part 2: Size of Smallest directory larger than {space_needed}: {dirs_8m[-1]}')


if __name__ == '__main__':
    day07(DATAFILE)
