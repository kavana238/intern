import numpy as np

pm = np.array([85, 90, 78, 120, 95, 130, 100])

print("Average:", np.mean(pm))
print("Unhealthy Days:", pm[pm > 100])
print("Percentage Unhealthy:", (np.sum(pm > 100) / len(pm)) * 100, "%")

