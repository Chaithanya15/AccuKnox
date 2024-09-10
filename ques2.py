# Do Django signals run in the same thread as the caller?
#Answer: Yes, Django signals run in the same thread as the caller by default. This means that the execution of the signal handlers occurs in the same thread that sent the signal.
import threading
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}")

# Sending the signal
print(f"Main thread before sending signal: {threading.current_thread().name}")
my_signal.send(sender=None)
print(f"Main thread after sending signal: {threading.current_thread().name}")


#When you run this code, the output will show that the receiver is running in the same
#thread as the main thread, confirming that signals are processed in the same thread as the caller.
