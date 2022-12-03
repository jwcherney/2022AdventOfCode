REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
DATAFILE = REAL_DATAFILE

SCORE_R = 1
SCORE_P = 2
SCORE_S = 3
WIN = 6
TIE = 3
LOSS = 0


def part_one_rps_score(choices):
    if choices[0] == "A":
        if choices[1] == "X":
            return_value = SCORE_R + TIE
        elif choices[1] == "Y":
            return_value = SCORE_P + WIN
        elif choices[1] == "Z":
            return_value = SCORE_S + LOSS
        else:
            return_value = 0
    elif choices[0] == "B":
        if choices[1] == "X":
            return_value = SCORE_R + LOSS
        elif choices[1] == "Y":
            return_value = SCORE_P + TIE
        elif choices[1] == "Z":
            return_value = SCORE_S + WIN
        else:
            return_value = 0
    elif choices[0] == "C":
        if choices[1] == "X":
            return_value = SCORE_R + WIN
        elif choices[1] == "Y":
            return_value = SCORE_P + LOSS
        elif choices[1] == "Z":
            return_value = SCORE_S + TIE
        else:
            return_value = 0
    return return_value


def part_two_rps_score(choices):
    if choices[0] == "A":
        if choices[1] == "X":
            return_value = SCORE_S + LOSS
        elif choices[1] == "Y":
            return_value = SCORE_R + TIE
        elif choices[1] == "Z":
            return_value = SCORE_P + WIN
        else:
            return_value = 0
    elif choices[0] == "B":
        if choices[1] == "X":
            return_value = SCORE_R + LOSS
        elif choices[1] == "Y":
            return_value = SCORE_P + TIE
        elif choices[1] == "Z":
            return_value = SCORE_S + WIN
        else:
            return_value = 0
    elif choices[0] == "C":
        if choices[1] == "X":
            return_value = SCORE_P + LOSS
        elif choices[1] == "Y":
            return_value = SCORE_S + TIE
        elif choices[1] == "Z":
            return_value = SCORE_R + WIN
        else:
            return_value = 0
    return return_value


def day02(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    p1_score = 0
    p2_score = 0
    for line in input_data:
        line = line.strip()
        p1_score += part_one_rps_score(line.split())
        p2_score += part_two_rps_score(line.split())
    print(f'Part 1 Score = {p1_score}')
    print(f'Part 2 Score = {p2_score}')


if __name__ == '__main__':
    day02(DATAFILE)
