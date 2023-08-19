
# alphanum-counter

A simple library to get alphanumeric numbers in order 

    A0001, A0002, ..., A1000, B0001, ...

## Usage

    counter = AlphanumCounter()
    counter.next() # returns first value

### Arguments

#### start: set the value to start the counter.
    counter = AlphanumCounter(start='B23')  # default: A0001
    counter.next() # returns B23

#### alpha_num: number of alphabet positions in the beginning.
    counter = AlphanumCounter(alpha_num=1) # default: 1
    counter.next() # returns A001
*Note: Only one position is supported for now.*

#### max_num: maximum count until numbers are increased.
    counter = AlphanumCounter(max_num=10)  # default: 1000
    counter.next() # returns A01

Note: Based on the max_num provided the output will be formatted with corresponding number of zeroes.

max_num=10 -> A01

max_num=100 -> A001

max_num=1000 -> A0001
