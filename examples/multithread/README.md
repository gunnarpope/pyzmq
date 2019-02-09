## Multithreading in ZMQ
See the example in Fig 20 at [zeromq.org](http://zguide.zeromq.org/py:all#sockets-and-patterns). This example builds a proxy that takes requests from the client, and then distributes the request to multiple 'worker nodes' for processing. These worker nodes respont to the proxy when done and the result is returned to the client.

To run, do:

    $ python multithread.py

Then, open another terminal and do:

    $ python client
