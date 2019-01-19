# FireSim-Python
Wildfire Spread Simulator

This code implements some of Dr. Angela B. Shiflet's [Spreading of Fire](http://nifty.stanford.edu/2007/shiflet-fire/) assignment, part of the SIGCSE 2007 [Nifty Assignments](http://nifty.stanford.edu/) collection.

The code works, but is quite limited:
* The dimensions of the simulation grid are hard-coded.
* The core simulation algorithm is hard-coded and not parameterizable.
* There is no way to record/report results summary statistics.

Nevertheless, it's a cute toy, and could be grown into a more interesting application.

Caveat:
The simulator is not completely platform-portable.  
It uses .PNG image files, and this may cause it to fail, depending upon the Tcl/Tk you have available.  
Experements show that it will not work under Mac OSX using Python 3.6 and the Apple-supplied Tcl/Tk 8.5.
There's a [detailed summary of this topic](https://www.python.org/download/mac/tcltk/) available at the Python Software Foundation website.
