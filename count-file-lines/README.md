## Count File Lines

There are lots of programs for working with files on the command line. A classic
unix tool is `wc` - word count. It has a lot of features for counting how many
lines, words, or bytes are in a given file, and displaying that information.

Other common command-line utilities like `grep` filters lines based on whether
they match some pattern. 

In this exercise, you'll write a program that has a mix of those tools' functionality. 

Your program will take in the name of a file as input, then print out the number of lines in that file. As an option, it can also take in a string to filter the lines. If a string is provided, it should only count the lines that contain that string.

## Your Task

In `main.py`, write a line-count program that can filter lines based on a lookup
value. 

- Ask the user for a file name. A valid path has to be provided (see the section below on Input Validation)
- Ask the user for an optional lookup value:
    - If the user enters a value, count the lines containing this value
    - If the user presses enter to continue with no value, then there is no string value to look up. The program should count all the lines.

## Input Validation 

Your code should not break when the user enters a wrong value:
- Input file: You need to check if this file/path exists
- Usage Statement: When a user enters a wrong value -> the program is expected to print a guiding message for the user. 

## Starter Code

In `main.py`, follow the prompts in the comments.

The core functionality is in the `line_count` function. It has a 
[docstring](https://peps.python.org/pep-0257/#what-is-a-docstring)
explaining what the function does. Docstrings are a way of documenting a
function or module to explain their behavior. This docstring explains the 
parameters the function accepts, what return value to expect, and how it is
supposed to work.

## Testing

Run your program interactively to guide and validate it as you develop your
solution.

Run the automated tests to verify that your `line_count` function works as
expected. Note that the tests only check the `line_count` function, and you need
to verify the `show_line_counts` function manually.

## Expected Results

These are the transcripts from running the program interactively. The filenames
are entered by the user.

### Entering a nonexistent file name

```txt
Please enter a file name or path for line counting: non-existent-file.txt
Optional: Please enter a value for lookup - Press [Enter] for no value:
Error: Please enter a valid file name
```

### Entering a file name only

```txt
Please enter a file name or path for line counting: README.md
Optional: Please enter a value for lookup - Press [Enter] for no value:
Number of lines in file: 77
```

### File name and lookup value

```txt
Please enter a file name or path for line counting: README.md
Optional: Please enter a value for lookup - Press [Enter] for no value: file
Number of lines containing [file] is: 15
```
