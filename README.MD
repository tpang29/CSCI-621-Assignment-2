# Assignment

Using the provided pseudo-code and explanation of a recursive descent parser, implement a recursive descent parser in Python.

# Usage

- this program reads in a line of input and returns a success or failure message for each valid line of input
- the parser will execute when given a valid path to the input file
- be sure that the input file's last line of content ends in a new line character, otherwise incorrect results may be returned

## Example

- See the following for a demonstration
- python3 driver.py
```
User-MacBook-Pro:RDP user$ python3 driver.py
Enter file name: test.txt
256 15 400
success
166 16 225
success
4096
success
1073741824
success
Do you wish to continue? Enter 'y' or 'n': y
Enter file name: test2.txt
1 2 3 4 5
success
6 7 8 9 10
success
2 4 8 16
success
32 64 128 256
success
Do you wish to continue? Enter 'y' or 'n': n
```

## Content of test.txt
```
2^2^3, 15, 20^2
166, 2^4, 15^2
2^12
2^30

```

## Content of test2.txt
```
1, 2, 3, 4, 5
6, 7, 8, 9, 10
2^1, 2^2, 2^3, 2^4
2^5, 2^6, 2^7, 2^8

```

