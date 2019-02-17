
"""
subscriber.py

A simple example of a Pub-Sub connection using ZeroMQ.
The Subscriber recieves the time from the Publisher each second.

To run, open a terminal and enter:
$ python publisher.py

After that, open any amount of clients in a new terminal to subscribe to
the publisher by entering:
$ python client.py

"""

#-----------------------------------------------------------------------------
#  Original Copyright (c) 2010 Brian Granger
#  Edits Copyright (c) 2019 Gunnar Pope
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
#-----------------------------------------------------------------------------

import time
import zmq

address="tcp://127.0.0.1:5555"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(address)
socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))

print('Starting A Subsciber....')
while True:
    try:
        text = socket.recv()
        print(text)
    except ( KeyboardInterrupt, SystemExit ):
        socket.term()                                                  # .term  ALWAYS!
        context.close()                                                     # .close ALWAYS!
        break
