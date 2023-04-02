def mergesort(array):
    if len(array) > 1:
        # Use middle as partition
        middle = len(array) // 2

        # Create temp arrays for hold the left and right half
        left_array = array[:middle]
        right_array = array[middle:]

        # Call mergesort recursively for left half of array
        # and then for the right half of the array
        mergesort(left_array)
        mergesort(right_array)

        # Set iterators
        i = 0
        j = 0
        k = 0

        # Copy temp array to each array half
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Check to ensure all temp data was copied back to our array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


if __name__ == '__main__':
    array = [3, 5, 8, 2, 13, 7, 3, 3, 20, 65, 1]
    print("Starting Array:")
    print(array)

    mergesort(array)

    print("Sorted Array:")
    print(array)
