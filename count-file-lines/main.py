# TODO: Import a module to help you with files
import os
import argparse
import re

def show_line_counts():
    # TODO: 
    # get filename from the user and, optionally, a lookup value
    # get the line count from "file_line_count" and print results

    # Read filename
    file_name = input("Please enter a file name or path for line counting: ")

    # Optionally include a lookup value
    lookup_value = input("Optional: Please enter a value lookup - Press [Enter] for no value: ")

    # Check if file exists
    if not os.path.exists(file_name):
        print("Error: Please enter a valid file name")
        return
    
    if len(lookup_value) > 0:
        print(f"Number of lines containing [{lookup_value}] is: {str(line_count(file_name, lookup_value))}")
    else:
        print(f"Number of lines in file: {str(line_count(file_name, lookup_value))}")

def line_count(filename: str, lookup_value: str) -> int:
    """
    Counts the number of lines in file. 
    If a lookup value is present, only counts lines that contain that value
    If the file does not exist, returns -1 
    :param: filename: name of the file to count lines from
    :param: lookup_value: string value to lookup for within the file
    :return: int number of lines matching lookup value, or -1
    """
    if not os.path.exists(filename):
        return -1
    
    lines = []
    matches = []
    # Open file for reading
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())

    if len(lines) > 0 and lines[-1] == '':
        lines.pop()
    
    for line in lines:
        # For each line
        # Look for a match of the lookup value if it was provided else matches an empty string which matches everything
        match = re.search(rf"{lookup_value}", line.strip(), re.IGNORECASE)
        if match is not None:
            # Append the matched lookup value
            matches.append(match.group())

    # Return the number of lines
    return len(matches)



if __name__ == "__main__":
    # TODO: Call function here
    parser = argparse.ArgumentParser(description="Count File Lines")
    show_line_counts()
