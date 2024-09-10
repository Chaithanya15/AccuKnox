#By default, do Django signals run in the same database transaction as the caller?
#Answer: Yes, by default, Django signals run in the same database transaction as the caller. If a signal is sent within a transaction, the receivers will also be executed within that same transaction.

from django.db import transaction
from django.dispatch import Signal, receiver
from django.db import models

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver executed")
    # This will raise an exception to demonstrate transaction rollback
    raise Exception("Simulating an error")

# Using a transaction
try:
    with transaction.atomic():
        MyModel.objects.create(name='Test')
        print("Signal about to be sent")
        my_signal.send(sender=None)
except Exception as e:
    print(f"Transaction rolled back due to: {e}")

# Check if the object was created
print(f"Count of MyModel objects: {MyModel.objects.count()}")
#In this code, the signal is sent inside a transaction. When the receiver raises an exception, the transaction is rolled back, and the object created prior to sending the signal is not saved in the database.
#The count of MyModel objects remains zero, demonstrating that the signal ran in the same transaction as the caller.
