def read_csv_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

read_csv_file('data.csv')