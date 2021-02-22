'''A demo is available in question4demo.jpynb'''

#calculate input using 4-connectivity
#use pandas to read the input file
import pandas as pd
#use numpy to write array into files
import numpy as np
#use skimage to determine the connectivity and generate the labelled matrix
#explainations referred to https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.label
from skimage import measure

data = pd.read_csv('input_question_4',delim_whitespace=True,header=None)
#two pixels are connected when they are neighbors like 4-connectivity and have the same value, in this case, both equal to 1
#if they are neighbors, they are assigned with a same number/index to indicate they are connected
#starting from 1
#the function goes through the input matrix/dataset row by row
#connectivity=1 is the same as the 4-connectivity described in the document
all_labels = measure.label(data,connectivity=1)
#return a numpy darray with labels
#where all connected regions are assigned the same integer value
np.savetxt('output_question_4.txt',all_labels,fmt="%d",delimiter=' ')
