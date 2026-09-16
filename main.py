def main_cleaner(originalCSV, CleanedCSV):
    cleaned_data = read_csv_file(originalCSV)
    check_row_lengths(cleaned_data)
    new_file(cleaned_data, CleanedCSV)

#strips lines of whitespace and adds to people list 
def read_csv_file(filename):
    with open(filename, "r") as file:
        people = []
        for line in file:
            stripped_line = line.strip()
            if stripped_line == "":
                continue
            else:
                people.append(stripped_line)
        return people

#Counts the total lines in the csv
def count_rows(filename):
    with open(filename, "r") as file:
        line_total = 0
        for line in file:
            line_total += 1
        return line_total

#Checks the row lengths
def check_row_lengths(rows):
    header = rows[0]
    column_count = len(header.split(","))
    for i, row in enumerate(rows[1:]):
        if len(row.split(",")) != column_count:
            print(f"Broken Row: {i+2}, Data: {row}")
        else:
            print(f"row {i+2} is good")

# writes cleaned data to new file
def new_file(rows, filename):
    with open(filename, "w") as new_data:
        for row in rows:
            new_data.write(row)
            new_data.write("\n")


#Clean the dataset
main_cleaner("data.csv", "clean_data.csv")