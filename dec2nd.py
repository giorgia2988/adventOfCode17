### December 1st

def first_ex(puzzle):

    all_diff = []
    for el in puzzle:
        number = [int(digit) for digit in el]
        all_diff.append(max(number)-min(number))

    return sum(all_diff)

def second_ex(puzzle):

    rows_div = []
    for el in puzzle:
        number = [int(digit) for digit in el]
        div = []
        for i in range(len(number)):
            for j in range(0, len(number)):
                if ((number[i]%number[j])==0 or (number[j]%number[i])==0)  and (i!=j):
                    div.append(number[i]//number[j])

        rows_div.append(sum(div))

    return sum(rows_div)

if __name__ == '__main__':

    input_path = './input_dec2nd.txt'
    puzzle = open(input_path).read().strip()
    puzzle = [el.split('\t') for el in puzzle.split('\n')]

    result_first = first_ex(puzzle)
    print('Result: (first_ex): %d' %result_first)

    result_second = second_ex(puzzle)
    print('Result: (second_ex): %d' %result_second)
