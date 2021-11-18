import random
code = ''.join((random.choice('defghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-') for i in range(10)))
print(code)
