# Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].

def make_it_big(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

arr1 = [-1,3,5,-5]

print(make_it_big(arr1))

# Create a function that takes an array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

def print_low_return_high(array):
    lowest = min(array)
    highest = max(array)
    print("Lowest value:", lowest)
    return highest

numbers = [0,3,9,2,77]
highest_value = print_low_return_high(numbers)
print("Highest Value:", highest_value)

# Build a function that takes an array of numbers. The function should print the second-to-last value in the array, and return first odd value in the array.

def print_second_to_last_return_first_odd(numbers):
    second_to_last = numbers[-2]
    first_odd = next((num for num in numbers if num % 2 != 0), None)
    print("Second-to-last value:", second_to_last)
    return first_odd

numbers = [2, 4, 6, 9, 10, 11, 12, 13, 18]
odd_value = print_second_to_last_return_first_odd(numbers)
print("First odd value:", odd_value)


# Given an array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.

def double_vision(numbers):
    doubled_list = []
    for i in range(len(numbers)):
        doubled_num = numbers[i] * 2
        doubled_list.append(doubled_num)
    return doubled_list

arr1 = [1,2,3]
print("Original Numbers:", arr1)
print("Doubled Numbers:", double_vision(arr1))

# Given an array of numbers, create a function to replace last value with the number of positive values. Example,  countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.

def count_positives(arr):
    count = sum(1 for num in arr if num >0)
    arr[-1] = count
    return arr

arr1 = [-1,1,1,1]
modified_arr = count_positives(arr1)
print(modified_arr)

# Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

# Example [1,1,2,5,5,5,10,10,10]

# Output:

# That's Odd

# That's Even

def check_odd_even(array):
    count_odd = 0
    count_even = 0

    for num in array:
        if num % 2 == 0:  # Even number
            count_odd = 0
            count_even += 1
            if count_even == 3:
                print("Even more so!")
                count_even = 0
        else:  # Odd number
            count_even = 0
            count_odd += 1
            if count_odd == 3:
                print("That's odd!")
                count_odd = 0

arr1 = [1, 1, 2, 5, 5, 5, 10, 10, 10]
check_odd_even(arr1)

# Given an array, add 1 to the value located at each odd indices of the array ([1], [3], etc.), console.log all values and return arr.

# Example [1,2,3,4,5,6] would become [1,3,3,5,5,7]

def increment_the_seconds(array):
    for i in range(len(array)):
        if i % 2 == 1:
            array[i] += 1
    return array

arr1 = [1,2,3,4,5,6]
print(increment_the_seconds(arr1))

# You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index, replace the first value with the length of the last string – and return the array.

# Example ['this', 'is', 'an', 'array']

# Output [5,4,2,2]

def previous_lengths(array):
    if len(array) == 0:
        return "There is no information."
    n = len(array)
    prev_length = len(array[n-1])
    for i in range(n):
        curr_length = len(array[i])
        array[i] = prev_length
        prev_length = curr_length
    return array

arr1 = ['this', 'is', 'an', 'array']
updated_arr = previous_lengths(arr1)
print(updated_arr)

# Build a function that accepts an array. Return a new array with all values except the first index, adding 7 to each. Do not alter the original array.

#  Example [1,2,3,4,5]

# Output [9,10,11,12]

def add_seven_to_most(arr):
    seven_added = []
    for i in range(1, len(arr)):
        add_7 = arr[i] + 7
        seven_added.append(add_7)
    return seven_added

arr1 = [1,2,3,4,5]
print(add_seven_to_most(arr1))

# Given array, write a function to reverse values, in-place. Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].

def reverse_array(array):
    start = 0
    end = len(array)-1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

arr = [3, 1, 6, 4, 2]
print(reverse_array(arr))

# Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

def negative_outlook(arr):
    negative_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            negative_value = -arr[i]
        else:
            negative_value = arr[i]
        negative_arr.append(negative_value)
    return negative_arr

arr1 = [1, -3, 5]
print(negative_outlook(arr1))

# Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.

# Example [1,2,'food',5]

# Output: yummy

def always_hungry(arr):
    found_food = False
    for i in range(len(arr)):
        if arr[i] == "food":
            print("Yummy")
            found_food = True
    if not found_food:
        print("Im Hungry")


arr1 = [1,2,"food",5]
always_hungry(arr1)

# Given array, swap first and last, third and third-to-last, etc. Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true].  Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

def swap_elements(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 2
        end -= 2

    return arr

arr1 = [True, 42, "Ada", 2, "pizza"]
print(swap_elements(arr1))

arr2 = [1, 2, 3, 4, 5, 6]
print(swap_elements(arr2))

# Given array arr and number num, multiply each arr value by num, and return the changed arr.

# Example scaleArr([1,2,3,4,5],3) = 3,6,9,12,15

def scale_array(arr, num):
    scaled_array = []
    for i in range(len(arr)):
        multiplied_num = arr[i] * num
        scaled_array.append(multiplied_num)
    return scaled_array

print(scale_array([1,2,3,4,5], 3))