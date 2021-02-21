'''A demo is available in question1demo.jpynb'''
from collections import Counter
# used this function to cound the number of directions in tuples
import csv
#import this library to write the output into files

#tup = (row, column, direction, confirmed sum)
#calculate the current summation for the coordinant stored as tuple
def total_sum(tup):
    summation = (1+tup[0])*tup[0]/2 + tup[3]+1*(tup[1]-1)
    return summation

#the length of operations should be "row_num+col_num-2"
#I started the walk of paths from the left bottom corner, and trace back towards the right up corner
#the default settings of the paths will be:
#from the coordinant(#row, #column), move up till the first row, then move left till the first column
#in the function "walk", it started to simulate the described selection of paths,
#and record the confirmed operations
#confirmed_sum is used as a stored variable for dynamic programming, since funcion "walk"
#need to calculate the summations of operations for comparison
#recording the confirmed_sum and confirmed operations meaning the steps are confirmed and
#are no longer needed to be calculated again
#in the end, the funcion "walk" updated the global variables operation and confirmed_sum,
#doesn't return other variables
operations = []
confirmed_sum = 0
def walk(row_num,col_num,desired_num):
    global operations
    global confirmed_sum
    operations = []
    confirmed_sum = 0
    for i in range(0,row_num+col_num-2):
        current_operation = (row_num,col_num,'U',confirmed_sum)
        if col_num-1 >0:
            #assume move left, add the possible number first
            #if move up in the end, minus the current row num, plus the next row num
            confirmed_sum += row_num
            next_operation = (row_num,col_num-1,'L',confirmed_sum)
        s = total_sum(current_operation)
        s2 = total_sum(next_operation)
        #print(desired_num, s,s2,operations)
        if desired_num > s and desired_num < s2:
            #then the desired operation would be go upward
            operations.append(current_operation)
            #largest number in the map
            row_num -= 1
        elif desired_num > s and desired_num > s2:
            #then the desired operation should go left, looking for larger possible paths
            #i set the function to favor moving left more than moving up in order to find
            #the corrent path
            operations.append(next_operation)
            col_num-=1
            current_operation = (row_num,col_num,'U',confirmed_sum)
            next_operation = (row_num,col_num-1,'L',confirmed_sum)
        elif desired_num < s and desired_num < s2:
            #in the case of the desired num is smaller than current operation and next operation
            #cannot move leftward anymore
            #return back to the current operation, and move upward (rownum-1)
            operations.append(current_operation)
            confirmed_sum -= row_num
            row_num-=1
            current_operation = (row_num,col_num,'U',confirmed_sum)
            confirmed_sum += row_num
            next_operation = (row_num,col_num-1,'L',confirmed_sum)
        elif desired_num == s:
            operations.append(current_operation)
            break
        elif desired_num == s2:
            operations.append(next_operation)
            break
#the "absence" of other items indicate default sate for the rest of the operations

#this function is a reconstruction of the operations after the steps are confirmed
def retrieve(row_num,col_num):
    global operations
    ndefault = len(operations)
    count =  Counter(elem[2] for elem in operations)
    #first record all the default movement, first go right then go down
    #the math works because the number of movements on row-level and column-level
    #is fixed, either equal to row_num-1 or col_num-1
    path = 'R'* (col_num-1-count['L'])+'D'* (row_num-1-count['U'])
    for i in range(ndefault,0,-1):
        if operations[i-1][2] == 'L':
            path += 'R'
        else:
            path += 'D'
    return path

#write down outputs into files
want_num_for_9_9_matrix = [65,72,90,110]
want_num_for_large_matrix = [87127231192,5994891682]

path = []
path_large = []

for item in want_num_for_9_9_matrix:
    walk(9,9,item)
    path.append(retrieve(9,9))

for item in want_num_for_large_matrix:
    walk(90000,100000,item)
    path_large.append(retrieve(90000,100000))

with open('output question 1.txt', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(zip(want_num_for_9_9_matrix, path))
    writer.writerow('')
    writer.writerows(zip(want_num_for_large_matrix, path_large))
