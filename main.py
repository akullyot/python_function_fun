#Purpose : A function that finds the maximum of three numbers and returns it
#Params  :  n many numbers
def max_num(*numbers):
    for number in numbers:
        assert isinstance(number, int), 'Please only input integers as arguments'
    current_max = 0
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max


#Purpose : Multiplies all numbers within a list
#Params  : A list of n numbers
def multi_list(number_list):
    #base case: your list is empty
    if not number_list:
        return 1
    #take the current 0th element and multiply the recursive call of the numbers list 
    # with the 0th element removed
    return number_list[0] * multi_list(number_list[1:])


#Purpose : reverses any given string and returns it 
#Params  : A string
def rev_string_recursive(string: str):
    assert isinstance(string, str), 'We can only reverse strings!'
    # The base case: your string is length 0
    if len(string) == 0:
        return string
    else:
        # call reverse with the first element removed of the current string removed
        # , and tack that on behind the next recursive call
        return rev_string_recursive(string[1:]) + string[0]


#Purpose: Checks wether a the middle number falls within range of the other two
#         (order does not matter for the flanks)
#Params: List of 3 numbers, where the middle number is being checked for range
def num_within(number_list):
    assert len(number_list) == 3, 'Please input a list of 3 numbers only'
    if number_list[0] >= number_list[1] and number_list[2] <= number_list[1]:
        return True
    elif number_list[0] <= number_list[1] and number_list[2] >= number_list[1]:
        return True
    else:
        return False


#Purpose: Prints out the first n rows of pascals triangle
#         (In a pasc. triangle each number is the two numbers added together)
#Params: a number n of desired pascal rows and a number apex that defines what the triangle starts at
def pascal_traingle_2D_array(n:int, apex:int =1):
    assert isinstance(n, int), 'Please give a INTEGER number corresponding to the desired number of rows printed.'
    assert isinstance(apex, int), 'Please give a INTEGER number corresponding to the desired apex number of your pascal triangle.'
    # first make an nxn 2d array of 0s of the needed length
    array = [[0 for x in range(n)] 
			for y in range(n)] 
    #iterate over your rows, starting at the apex
    for row_index in range(0,n):
        for element_index in range(0, row_index +1):
            # The 1st and last values of a triangle row are always 1 because they only have one element above them  
            #   and that's the apex which we have defined as 1
            if (element_index == 0 or element_index == row_index):
                array[row_index][element_index] = apex
            else:
                #since we defined top down we can just look at the two above in array
                # (since our 2d array is a right triangle essentially its the element index directly above and one to the left)
                array[row_index][element_index] = array[row_index -1][element_index] + array[row_index -1][element_index-1]
        # deleting the zeroes for prettier printing
        del array[row_index][row_index +1 : n]
    # using the unpacking operator 
    for row in array:
        print(*row, sep=" ")

#Unit Tests
if __name__ == "__main__":
    print('max_num fxn tests:')
    print(max_num(5,6,9, 90, 2, 5))
    print(max_num(1))
    print("_"*40)

    print('mult_list fxn tests:')
    print(multi_list([5,10,15,20]))
    print(multi_list([3]))
    print("_"*40)

    print("rev_string_recursive fxn tests:")
    print(rev_string_recursive("Annie Ullyot"))
    print(rev_string_recursive("abcdefghi"))
    print("_"*40)

    print('num_within fxn tests:')
    print(num_within([1,5,10]))
    print(num_within([-5, 15, 10]))
    print(num_within([50,25,-10]))
    print(num_within([5,5,5]))
    print("_"*40)


    print(" pascal_traingle_2D_array fxn tests:")
    pascal_traingle_2D_array(5)
    pascal_traingle_2D_array(10,2)


