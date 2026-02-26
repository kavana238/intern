import numpy as np
import time

arr = np.arange(1_000_000)

start = time.time()
result = []

for i in arr:
    result.append(i * 2)

end = time.time()
print("Loop time:", end - start)