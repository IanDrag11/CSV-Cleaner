def read_csv_file(filename):
    with open(filename, "r") as file:
        people = []
        for line in file:
            x = line.strip()
            if x == "":
                continue
            else:
                people.append(x)
        return people

cleaned_data = read_csv_file('data.csv')
print(cleaned_data)

def count_rows(filename):
    with open(filename, "r") as file:
        line_total = 0
        for line in file:
            line_total += 1
        return line_total

print(count_rows('data.csv'))





