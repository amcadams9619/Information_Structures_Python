# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/29/18
Homework 4, Question 11.1
Print distinct numbers
"""

def sumColumn(m, columnIndex):
    """
    Loops thorugh the rows and returns the total values for each column
    
    Input param 1: Matrix 0
    Input param 2: Matrix 1
    Input param 3: Matrix 2
    """
    #Initialize total to zero
    total = 0
    
    #loop through the rows and add up the totals
    for column_num in range(3):
        total += m[column_num][columnIndex]
    return total
    
def matrix_calculation():
    """
    Asks for user input, and adds numbers to list
    
    Input param 1: Matrix 0
    Input param 2: Matrix 1
    Input param 3: Matrix 2
    """
    #Initialize rows, columns, and matrix
    number_rows = 3
    number_columns = 4
    matrix = []
    
    #Asks for user input
    for row_num_string in range(number_rows):
        user_input = input('Enter a 3-by-4 matrix row for row {}: '\
                           .format(str(row_num_string)))
        numbers = user_input.split(' ') #Separating numbers by spaces
        number_list = [float(new_num) for new_num in numbers] #Converting entries to floating numbers
        matrix.append(number_list) #Appending the matrix with the new floating numbers established in the the number_list
    print('\n') #Adding spacing between input and output
    
    #Print out the totals for each column in the matrix through incorporating sumColumn function
    for column_num_string in range(number_columns):
        total_sum = sumColumn(matrix, column_num_string)
        print('Sum of the elements in column {} is {}' \
              .format(column_num_string, total_sum))

if __name__ == "__main__": 
    matrix_calculation() #Call the matrix calculation function