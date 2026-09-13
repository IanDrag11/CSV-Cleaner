def read_csv_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

read_csv_file('data.csv')

def count_rows(filename):
    with open(filename, "r") as file:
        line_total = 0
        for line in file:
            line_total += 1
        return line_total

print(count_rows('data.csv'))




