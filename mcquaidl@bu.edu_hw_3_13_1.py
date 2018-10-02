# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/22/18
Homework 3, Question 13.1
Remove Text
"""

def main():
    """
    Open a file and remove a select phrase
    
    Input param 1: file_name -- the file name to open
    input param 2: remove_text --the phrase or text to be removed
    """
    
    #User enters a file they wish to open
    file_name = input('Enter a file name (i.e. Test.txt): ').strip()
    
    #What string does the user wish to remove
    remove_text = input('Enter the string to be removed: ')
    
    #Open the file
    infile = open(file_name, "r")
    
    #Copy the files lines
    strng =[]
    
    #Remove the text
    for line in infile:
        changed_text = line.replace(remove_text, '')
        strng.append(changed_text)
    
    #Close file
    infile.close()
    
    #Write data to the file
    outfile = open(file_name, "w")
    
    #Overwrite file
    for line in strng:
        outfile.write(line)
    
    #Close file and print 'Done'
    outfile.close()
    print('Done')
    
main () #Call the main function