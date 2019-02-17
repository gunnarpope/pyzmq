## ZeroMQ Publish-Subscribe Example
by: Gunnar Pope 2/17/19

This is an example of a one-to-many network connection in ZeroMQ. It is asynchronous, quick, and scalable.

In this example, the publisher prints out the local time for all subscribers to digest.

To begin, start two separate terminals to simulate two different client 'subscriber' nodes:

    [terminal 1]
    $ python subscriber.py

    [terminal 2]
    $ python subscriber.py


Now that the clients are listening, start up the publisher node.

    [terminal 3]
    $ python publisher.py

The outputs are:

    [publisher]
    ~/repos/zeromq/pyzmq/examples/pubsub $ python publisher.py
    Starting The Publisher....
    Sending Time:  Sun Feb 17 09:13:47 2019
    Sending Time:  Sun Feb 17 09:13:48 2019
    Sending Time:  Sun Feb 17 09:13:49 2019
    Sending Time:  Sun Feb 17 09:13:50 2019

    [subscriber 1]
    ~/repos/zeromq/pyzmq/examples/pubsub $ python subscriber.py
    Starting A Subsciber....
    b'Sun Feb 17 09:13:48 2019'
    b'Sun Feb 17 09:13:49 2019'
    b'Sun Feb 17 09:13:50 2019'
    b'Sun Feb 17 09:13:51 2019'
    b'Sun Feb 17 09:13:52 2019'
    b'Sun Feb 17 09:13:53 2019'

    [subscriber 2]
    ~/repos/zeromq/pyzmq/examples/pubsub $ python subscriber.py
    Starting A Subsciber....
    b'Sun Feb 17 09:13:48 2019'
    b'Sun Feb 17 09:13:49 2019'
    b'Sun Feb 17 09:13:50 2019'
    b'Sun Feb 17 09:13:51 2019'
    b'Sun Feb 17 09:13:52 2019'
    b'Sun Feb 17 09:13:53 2019'


Even though we started the subscribers first, we still miss the first publication at 9:13:47. Why? I will have to look into this later.
