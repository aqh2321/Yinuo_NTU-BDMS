'''A demo is available in question7demo.jpynb'''

import pandas as pd
import numpy as np
#use to calculate the coordinates
from math import floor

'''7-1'''
input_coordinate_7_1= pd.read_csv('input_coordinates_7_1.txt',delim_whitespace=True)
input_indices_7_1= pd.read_csv('input_index_7_1.txt',delim_whitespace=True).to_numpy()

coordinates_7_1=list(input_coordinate_7_1.itertuples(index=False, name=None))

#for a grim of (50,57)
def coordinate_to_index_7_1(coordinates):
    output = []
    for x1,x2 in coordinates:
        output.append(x1+50*x2)
    return output
#for a grim of (50,57)
#using floor since i need to know how many "rows" was before the index
def index_to_coordinate_7_1(index):
    output = []
    for i in index:
        output.append([int(i-50*floor(i/50)),floor(i/50)])
    return output
output_array_7_1 = coordinate_to_index_7_1(coordinates_7_1)
output_array_index_7_1 = pd.DataFrame(index_to_coordinate_7_1(input_indices_7_1),columns = ['x1','x2'])

np.savetxt('output_index_7_1.txt',output_array_7_1,fmt='%d',header = 'index')
output_array_index_7_1.to_csv('output_coordinates_7_1.txt', index=None, sep=' ')

'''7-2'''
input_coordinate= pd.read_csv('input_coordinates_7_2.txt',delim_whitespace=True)
input_indices= pd.read_csv('input_index_7_2.txt',delim_whitespace=True).to_numpy()
coordinates=list(input_coordinate.itertuples(index=False, name=None))

#for a grim of (L1, L2, L3, L4, L5, L6)=(4, 8, 5, 9, 6, 7),
def coordinate_to_index(coordinates):
    output = []
    L = [4, 8, 5, 9, 6, 7]
    for item in coordinates:
        output.append(item[5]*L[0]*L[1]*L[2]*L[3]*L[4] + item[4]*L[0]*L[1]*L[2]*L[3]+
                     item[3]*L[0]*L[1]*L[2]+item[2]*L[0]*L[1]+item[1]*L[0]+item[0])
    return output
#for a grim of (50,57)
#using floor since i need to know how many "rows" was before the index
def index_to_coordinate(index):
    output = []
    L = [4, 8, 5, 9, 6, 7]
    for i in index:
        output.append([int(i-L[0]*floor(i/L[0])),floor(i % np.prod(np.array(L[:2])) / L[0]),
                       floor(i % np.prod(np.array(L[:3])) / np.prod(np.array(L[:2]))), floor(i % np.prod(np.array(L[:4])) / np.prod(np.array(L[:3]))),
                       floor(i % np.prod(np.array(L[:5])) / np.prod(np.array(L[:4]))), floor(i/np.prod(np.array(L[:-1])))])
    return output

output_array = coordinate_to_index(coordinates)
np.savetxt('output_index_7_2.txt',output_array,fmt='%d',header = 'index')
output_array_index = pd.DataFrame(index_to_coordinate(input_indices),columns = ['x1','x2','x3','x4','x5','x6'])
output_array_index.to_csv('output_coordinates_7_2.txt', index=None, sep=' ')
