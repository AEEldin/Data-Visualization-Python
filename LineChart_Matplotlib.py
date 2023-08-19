'''
Prepare the matplotlib library.
Python version 3.8 is the most stable version, used in the different tutorials.

python3 --version
pip3 --version
pip3 install matplotlib
'''


import matplotlib                # first step is to import the library
print(matplotlib.__version__)    # let's first check the version used


# part 1

# pyplot is a submodule where most of the Matplotlib utilities exists

import matplotlib.pyplot as plt  # let's import such submodule with an alias of plt


# as a simple start, let's draw a line from start point (10,100) to end point (20,250):

horizontal = [10,20]       # the horizontal axis starts at 10 and ends at 20
vertical   = [100,250]     # the vertical axis starts at 100 and ends at 250

plt.plot(horizontal, vertical)   # let's design the graph

"""
plot() is used to first mark points and draw lines (by default) between them
plot() accepts some inputs:
First input is an array containing the points of the x-axis.
Second input is an array containing the points of the y-axis.
"""
plt.show()                                  # let's display the graph







# part 2
# now, let's draw a graph between a set of 4 sequential points:

import matplotlib.pyplot as plt  # let's import such submodule with an alias of plt


horizontal = [1, 2, 5, 7]
vertical = [3, 7, 2, 8]
  
plt.plot(horizontal, vertical) 
plt.show()                  







# part 3
# let's add some titles and labels with font

import matplotlib.pyplot as plt  # let's import such submodule with an alias of plt

horizontal = [1, 2, 5, 7]
vertical = [3, 7, 2, 8]

plt.plot(horizontal, vertical)   

font1 = {'family':'ariel','color':'blue','size':12}             # let's define one formate
font2 = {'family':'serif','color':'red','size':10}              # let's define another formate

plt.title("Simple Plot", fontdict = font1, loc = 'center')      # let's include a title
plt.ylabel("y-axis", fontdict = font2)                          # let's include a label on the vertical axis
plt.xlabel("x-axis", fontdict = font2)                          # let's include a label on the horizonatal axis
plt.show()                                                      # let's display the graph




# part 4
import matplotlib.pyplot as plt

horizontal = [1, 2, 5, 7]
vertical = [3, 7, 2, 8]


"""
plot() also accepts more inputs:
First input is an array containing the points of the x-axis.
Second input is an array containing the points of the y-axis.
Third input (optional) is used to plot the points using various markers (e.g., 'o', 'x', '*')

    you can change the style of the line using linestyle (ls), color, and linewidth (lw) parameters:
        plt.plot(horizontal, vertical, ls = ':', color = 'r', lw = '8.5')  
            where ':' is for dotted line, - for solid, -- for dashed
            where 'r' is for red color, 'g' for green, 'b' for blue

    you can display the points without the lines:
        plt.plot(horizontal, vertical, '*')  

    you can also display the points on the lines and define the size of them with markersize (ms) parameter:
        plt.plot(horizontal, vertical, marker = '*', ms = 20)  

    you can also display the points on the lines, define the size, and set the color of the markers with markerfacecolor (mfc) parameter:
        plt.plot(horizontal, vertical, marker = '*', ms = 20, mfc = 'r')              
            where 'r' is for red color, 'g' for green, 'b' for blue
   
    you can also change the format/shape of the line, the color, and the point marker using the shortcut string notation parameter
    This parameter is called fmt and is written with this syntax: marker|line|color
        plt.plot(horizontal, vertical, '*:r') 
"""
  
plt.plot(horizontal, vertical, ls = ':', color = 'r', lw = '8.5', marker = '*', ms = 20)  
plt.title("Simple Plot")    
plt.ylabel("y-axis")        
plt.xlabel("x-axis")        
plt.show()    





# part 5
# you can use plot() multiple times to draw many lines on the same diagram

import matplotlib.pyplot as plt

horizontal1 = [10,20]      
vertical1   = [100,250]    
plt.plot(horizontal1, vertical1) 

horizontal2 = [10, 20, 50, 70]
vertical2 = [30, 70, 20, 80]
plt.plot(horizontal2, vertical2) 

plt.show()




# part 6
# Display Multiple Plots
import matplotlib.pyplot as plt

'''
The subplot() function enables multiple plots in the layout of the output figure, the layout is arranges in a table formate with rows and columns.

The subplot() function accepts three parameters to describe the layout.
First argument represents the number of rows
Second argument represents the number of columns
Third argument represents the position in the layout
'''

horizontal1 = [10,20]      
vertical1   = [100,250]    
plt.subplot(1, 2, 1)            #the layout is 1 row, 2 columns, and this plot is in the first position
plt.plot(horizontal1, vertical1)
plt.title("First plot")

horizontal2 = [10, 20, 50, 70]
vertical2 = [30, 70, 20, 80]
plt.subplot(1, 2, 2)            #the layout is 1 row, 2 columns, and this plot is in the second position
plt.plot(horizontal2, vertical2) 
plt.title("Second plot")


plt.suptitle("All plots")       #add one title on the collection
plt.show()



#https://www.w3schools.com/python/matplotlib_markers.asp
