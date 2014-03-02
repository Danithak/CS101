#!/usr/bin/python

# Numbers in lists by SeanMc from forums
# Define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.


def numbers_in_lists(string):
  new_list = []
  sub_list = []
  biggest_number = 0
  for i in string:
    if int(i) > biggest_number:
      biggest_number = int(i)     # Updates largest number
      if sub_list:                # If next number is largest, appends entire 
        new_list.append(sub_list) # sublist to previous larger number.
        sub_list = []             # Resets sublist after appending
      new_list.append(int(i))     # Appends new largest number to the main list
    else:
      sub_list.append(int(i))     # Continues appending numbers to the sublist if they are smaller
  if sub_list:                    # After looping through all variables, checks to see if a 
    new_list.append(sub_list)     # sublist is still present, and appends if so. 
  return new_list
    

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
