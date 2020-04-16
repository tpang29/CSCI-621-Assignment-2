# CSCI-621: Programming Languages | Assignment 2

- Using the provided pseudo-code in [assignment-2-description](https://github.com/tpang29/CSCI-621-Assignment-2/blob/master/assignment-2-description.pdf), implement a recursive descent parser in Python.

# Usage

## Setup
- Python 3.x required
- Download the folder titled `src`
- Navigate into the `src` directory
- Verify that `driver.py`, `inputUtils.py`, and `recursiveDescentParser.py` exist, as well as the directory, `test_files`.
- Veify that the directory, `test_files`, contains three files titled, `test.txt`, `test2.txt`, and `test3.txt`. If not the contents of each are listed [below](#test-files). It is important to note that each test file ends with a new line character. `\r\n` or `\n`.

## Run
- `python driver.py` or `python3 driver.py`
- note that you will be prompted for a relative path. See [demo](#Demo) below.

## Test Files
- test.txt
```
2^2^3, 15, 20^2
166, 2^4, 15^2
2^12
2^30

```
- test2.txt
```
1, 2, 3, 4, 5
6, 7, 8, 9, 10
2^1, 2^2, 2^3, 2^4
2^5, 2^6, 2^7, 2^8

```
- test3.txt
```
2^2^3, 15, 20^2
166, 2^4, 15^2
2*30
2^12

```
# Demo
- You will be prompted to enter the relative file path from the `src` directory
- Note that an input message of "success" or "failure" will be printed to the console after each line of correctly parsed input
- The following output is divided with brief descriptions of program responses to the various input files
```
User-MacBook-Pro:src username$ python3 driver.py 
```
- Given correct relative file path
```
Enter relative file path or 'q' to exit: test_files/test.txt
256 15 400
success
166 16 225
success
4096
success
1073741824
success
```
- Given correct relative file path
```
Enter relative file path or 'q' to exit: test_files/test2.txt
1 2 3 4 5
success
6 7 8 9 10
success
2 4 8 16
success
32 64 128 256
success
```
- Given correct relative file path
```
Enter relative file path or 'q' to exit: test_files/test3.txt
256 15 400
success
166 16 225
success
failure
4096
success
```
- Given incorrect relative file path
```
Enter relative file path or 'q' to exit: test-files/test.txt
Invalid file path
```
- Exit program
```
Enter relative file path or 'q' to exit: q
User-MacBook-Pro:src username$ 
```
