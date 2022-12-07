REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
DATAFILE = REAL_DATAFILE

SCORE_R = 1
SCORE_P = 2
SCORE_S = 3
WIN = 6
TIE = 3
LOSS = 0

# ABC is row, XYZ is columns
PART_1_SCORE = [[SCORE_R + TIE, SCORE_P + WIN, SCORE_S + LOSS],
                [SCORE_R + LOSS, SCORE_P + TIE, SCORE_S + WIN],
                [SCORE_R + WIN, SCORE_P + LOSS, SCORE_S + TIE]]
PART_2_SCORE = [[SCORE_S + LOSS, SCORE_R + TIE, SCORE_P + WIN],
                [SCORE_R + LOSS, SCORE_P + TIE, SCORE_S + WIN],
                [SCORE_P + LOSS, SCORE_S + TIE, SCORE_R + WIN]]


def day02(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    p1_score = 0
    p2_score = 0
    for line in input_data:
        values = line.split()
        first = ord(values[0]) - ord('A')
        second = ord(values[1]) - ord('X')
        p1_score += PART_1_SCORE[first][second]
        p2_score += PART_2_SCORE[first][second]
    print(f'Part 1 Score = {p1_score}')
    print(f'Part 2 Score = {p2_score}')


if __name__ == '__main__':
    day02(DATAFILE)
