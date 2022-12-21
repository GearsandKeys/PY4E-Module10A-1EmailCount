# PY4E-Module010A-1EmailCount

## Assignment
1. Read and parse the “From” lines and pull out the addresses from the line. 
2. Count the number of messages from each person using a dictionary.
3. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
4. Sort the list in reverse order and print out the person who has the most commits.

## Sample Line:
```
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```

## Desired Output
```
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
```

## Starter Code
```
file_name = input("Enter a file name: ")
```

## Test
When your code is ready to test, run `pytest` in the terminal
