# File: main.py
# Directory: ciss450/a/a01/a01q09
# Author: Carl Dalebout

def mergesort(xs, verbose = False):
    """Merge sort algorithm implementation."""

    if len(xs) <= 1:  # base case
        if verbose:
            print(xs)
        return xs

    # divide xs in half and merge sort recursively
    half = len(xs) // 2
    left = mergesort(xs[:half], verbose)
    right = mergesort(xs[half:], verbose)

    def merge(left, right, verbose = False):
        """Merge sort merging function."""

        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        if verbose:
            print([left, right])

        result += left[left_index:]
        result += right[right_index:]

        if verbose:
            print(result)

        return result

    return merge(left, right, verbose)

if __name__ == '__main__':
    s = input()         # for instance enter "51,32,1,23,47" (w/o
                        # quotes) to sort [51, 32, 1, 23, 47]
    xs = [int(_) for _ in s.split(',') if _ != '']

    xs = mergesort(xs, verbose=True)
    print(xs)