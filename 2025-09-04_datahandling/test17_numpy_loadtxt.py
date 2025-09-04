import numpy as np

D = np.array([[1,2,3,],[4,5,6]])
np.savetxt('2025-09-04_datahandling/dataset/sampletxt.csv', D, delimiter=',')

loaded_data = np.loadtxt('./2025-09-04_datahandling/dataset/sampletxt.csv', delimiter=',', dtype=np.float32)

print('loaded_data.shape = ', loaded_data.shape)
print(loaded_data)