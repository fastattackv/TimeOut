# TimeOut
Python package to create timeouts in your code

## Example scripts
```
import TimeOut as To


def test():
    print("timeout reached!")


instance = To.TimeOut(5, test, infos=True)

instance.start()
```
In this example, we created a function 'test' to call when the timeout reaches the time.
We then created an instance of TimeOut with a time of 5 seconds, the command set to test and infos set to True so we can see what the timeout does.
This will print:
```
TimeOut started
TimeOut stopped
timeout reached!
```
_TimeOut started_ is printed when the line 5th line (_instance.start()_) is executed

_TimeOut stopped_ is printed when the timeout has wait the 5 seconds we told it

_timeout reached!_ is printed when our _test_ function is executed (when the timeout has wait the 5 seconds we told it)

```
import TimeOut as To
import time


def test():
    print("timeout reached!")


instance = To.TimeOut(5, test, infos=True)

instance.start()
time.sleep(2)
instance.reset()
```
This time, we create the same instance as the first example but 2 seconds after starting the timeout, we reset it, which stops the first timeout and starts a new one.
This will print:
```
TimeOut started
TimeOut stopped
TimeOut started
TimeOut stopped
timeout reached!
```

The first _TimeOut started_ is printed like in the first example

Then _TimeOut stopped_ and _TimeOut started_ are printed simultaneously, 2 seconds after starting the first timeout, when the line 8th line (_instance.reset()_) is executed

And finnaly, 7 seconds after we started the first timeout, _TimeOut stopped_ and _timeout reached!_ are printed when the second timeout has reached its end.


<sub>To pause, resume, handle errors and get more information on the timeout, check the documentation</sub>
