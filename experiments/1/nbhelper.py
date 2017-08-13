import matplotlib.pyplot as plt
import numpy


def plot(y, minx=-1, maxx=1):
    fig = plt.figure(figsize=(2,2))
    
    p = fig.add_subplot(1,1,1)
    p.plot(x, y, color='red')
    center_axes(p, minx, maxx)

# a plot for the identity activation function f(x) = x
def plot_identity():
    f_identity = x
    plot(f_identity)
    

# a plot for the relu activation function f(x) = max(0,x)
def plot_relu():
    f_relu = numpy.maximum(0.01, x) # so the line is still visible
    plot(f_relu)

def plot_logistic():
    f_log = 1 / (1+numpy.exp(-x))
    plot(f_log, -6, 6)

def plot_tanh():
    f_tanh = numpy.tanh(x)
    plot(f_tanh, -2, 2)
    
# remove frame, and put labeled axes through origin
def center_axes(p, xmin, xmax):
    p.set_xlim([xmin,xmax])
    p.set_ylim([-1,1])
    p.spines['left'].set_position('center')
    p.spines['bottom'].set_position('center')
    p.spines['right'].set_color('none')
    p.spines['top'].set_color('none')


    
# make some data to work with
x = numpy.linspace(-10,10,3000)
