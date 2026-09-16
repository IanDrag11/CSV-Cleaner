# CSV Cleaner
I created a simple Python CSV file that looks at each line, removes whitespace, and writes a cleaned version to a new file.

## What It Does
- Reads the csv and strips the whitespace from each row
- Skips blank and empty rows
- Checks if each row has the same number of colums as the header, and flags any that dont (with the line number)
- Writes the cleaned data to a new output file

# How To Run It
```python
main_cleaner("data.csv", "clean_data.csv")
```

This reads "data.csv", validates the lines and cleans it, and writes the result to "clean_data.csv".

# Why I Did This & What I Learned
This is my first project using Git/Github, and my first time writing multiple functions that work together as a pipeline. 
