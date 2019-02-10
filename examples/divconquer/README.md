## Multithreading using a Fan-In to Fan-Out model in ZMQ
See the example on p14 of zguide-py.pdf from Pieter Hintjens. Thanks for your work, Pieter. 

In this example, the `ventilator` sends out a series of 'wait' commands that, when summed up in series would total 2 seconds. This example divide the work up between multiple processes (Fan-out) to solve the problem in parallel, then combines the result with a Fan-In to publish the results to a local node.

To run, do:

    $ python tasksink.py

Then, open another terminal and do:

    $ python worker.py 

Finally, start the broadcast with the ventilator node:

    $ python ventilator.py

Output:

    $ ~/repos/pyzmq/examples/divconquer $ python ventilator.py 
    Press Enter when the workers are ready: 
    
    Sending tasks to workers...
    Total expected cost: 51729 msec

The program should finish much before then the expected time of completion.
