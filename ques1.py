#Question 1: Are Django signals executed synchronously or asynchronously by default?
#Answer: By default, Django signals are executed synchronously. This means that when a signal is sent, the connected receivers are executed immediately in the same thread of execution.
#from django.dispatch import Signal, receiver

import time

# Define a signal
my_signal = Signal()

# Define a receiver
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(2)  # Simulate a long-running task
    print("Receiver finished")

# Sending the signal
print("Sending signal")
my_signal.send(sender=None)
print("Signal sent")


#When you run this code, you will see that "Sending signal" is printed, followed by "Receiver started",
#then a 2-second delay, and finally "Receiver finished". This demonstrates that the signal is processed synchronously, blocking further execution until the receiver completes.
