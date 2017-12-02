### December 1st

def first_ex(puzzle):

    n_digit = len(puzzle)
    puzzle_select = []
    for d1, d2 in zip(puzzle, puzzle[1:]+ puzzle[0]):
        if d1 == d2:
            puzzle_select.append(d1)

    return sum([int(el) for el in puzzle_select])


def second_ex(puzzle):

    n_digit = len(puzzle)
    step = n_digit//2
    puzzle += puzzle[:step]
    puzzle_select = []
    for d in range(n_digit-step):
        if puzzle[d]==puzzle[d+step]:
            puzzle_select.append(puzzle[d])
            puzzle_select.append(puzzle[d+step])

    return sum([int(el) for el in puzzle_select])


if __name__ == '__main__':

    input_path = './input_dec1st.txt'
    puzzle = open(input_path).read().strip()

    result_first = first_ex(puzzle)
    print('Result: (first_ex): %d' %result_first)

    result_second = second_ex(puzzle)
    print('Result: (second_ex): %d' %result_second)
