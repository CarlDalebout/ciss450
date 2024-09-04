# File: main.py
# Directory: ciss450/a/a01/a01q09
# Author: Carl Dalebout

def mergesort(xs, verbose=False):
    # Put merge function here
    def mergesort_(xs, start, end, t, verbose=False):
        # To be completed
        if verbose:
            print(xs)

    t = [] # temporary array
    n = len(xs)
    mergesort_(xs, 0, n, t, verbose)

if __name__ == '__main__':
    s = input()         # for instance enter "51,32,1,23,47" (w/o
                        # quotes) to sort [51, 32, 1, 23, 47]
    xs = [int(_) for _ in s.split(',') if _ != '']

    # mergesort(xs, verbose=True)
    print(xs)
