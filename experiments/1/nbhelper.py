import matplotlib.pyplot as plt
import numpy

# a plot for the identity activation function f(x) = x
def plot_identity():
    f_identity = x
    fig = plt.figure(figsize=(2,2))
    
    p = fig.add_subplot(1,1,1)
    p.plot(x, f_identity, color='red')
    center_axes(p)
    

# a plot for the relu activation function f(x) = max(0,x)
def plot_relu():
    f_relu = numpy.maximum(0.01, x) # so the line is still visible
    fig = plt.figure(figsize=(2,2))

    p = fig.add_subplot(1,1,1)
    p.plot(x, f_relu, color='red')
    center_axes(p)

    
# remove frame, and put labeled axes through origin
def center_axes(p):
    p.set_xlim([-1,1])
    p.set_ylim([-1,1])
    p.spines['left'].set_position('center')
    p.spines['bottom'].set_position('center')
    p.spines['right'].set_color('none')
    p.spines['top'].set_color('none')


    
# make some data to work with
x = numpy.linspace(-1,1,30)
