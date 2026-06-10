import numpy as np
import matplotlib.pyplot as plt


IMP_0 = 377

width = 200
max_time = 200

ez = np.zeros(width)
hy = np.zeros(width)
result = np.zeros(max_time)

for time_step in range(max_time):
    # update magnetic field
    for index in range(0, width - 1):
        hy[index] += (ez[index + 1] - ez[index]) / IMP_0

    # update electric field
    for index in range(1, width):
        ez[index] += (hy[index] - hy[index - 1]) * IMP_0

    # add permanent source
    ez[0] += np.exp(-(time_step - 30) * (time_step - 30) / 100)

    if time_step == 30:
        result = np.copy(ez)

plt.plot(result)
plt.show()

