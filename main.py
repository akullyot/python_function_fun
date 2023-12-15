#Purpose : A function that finds the maximum of three numbers and returns it
#Params  : list of 3 numbers
def max_num(number_list):
    pass

#Purpose : Multiplies all numbers within a list
#Params  : A list of n numbers
def multi_list(number_list):
    pass

#Purpose : reverses any given string and returns it 
#Params  : A string
#Type 1  : recursive
def rev_string_recursive(string: str):
    assert isinstance(string, str), 'We can only reverse strings!'
    # The base case: your string is length 0
    if len(string) == 0:
        return string
    else:
        # call reverse with the first element removed of the current string removed
        # , and tack that on behind the next recursive call
        return rev_string_recursive(string[1:]) + string[0]

    
#Type 2  : loop through and add to the start of the output string
def rev_string_iterative(string):
    pass


#Purpose:
#Params:




#Unit Tests
print(rev_string_recursive("Annie Ullyot"))
print(rev_string_recursive("abcdefghi"))
#print(rev_string_recursive(12345)) ## Uncomment out to throw a typing error
