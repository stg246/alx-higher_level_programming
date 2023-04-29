#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.
    
    Args:
        list_of_integers (list): A list of integers
        
    Returns:
        int: A peak in the list
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    
    # Check edge cases
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n-1] >= list_of_integers[n-2]:
        return list_of_integers[n-1]
    
    # Binary search for a peak
    left, right = 1, n-2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid-1] and list_of_integers[mid] >= list_of_integers[mid+1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid-1]:
            right = mid - 1
        else:
            left = mid + 1
    
    # No peak found
    return None
