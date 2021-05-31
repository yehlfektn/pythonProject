import sys
import pandas as pd
import numpy as np

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

try:
    df = pd.read_csv(sys.argv[1], index_col=0)
except IOError:
    print("Error opening file: ", sys.argv[1])
    sys.exit()

try:
    cube_parameter = sys.argv[2]
    if cube_parameter != "cube225":
        if cube_parameter != "cube300":
            if cube_parameter != "cube375":
                if cube_parameter != "cube400":
                    raise IndexError
except IndexError:
    print("Please specify cube parameter: it should be one of these: cube225, cube300, cube375, cube400")
    sys.exit()

print(cube_parameter)
print(df)
df_result = pd.DataFrame(columns=['arrival_time', 'velocity', 'distance', 'channel'])
cube225 = pd.DataFrame(np.array([[2, 226991.1893],
                                 [3, 226991.1893],
                                 [4, 141509.717],
                                 [5, 162249.8074],
                                 [6, 150000],
                                 [7, 123693.1688],
                                 [8, 184932.4201]]),
                       columns=['sensor', 'distance'])

cube300 = pd.DataFrame(np.array([[2, 236220.2362],
                                 [3, 300000],
                                 [4, 313209.1953],
                                 [5, 164316.7673],
                                 [6, 250998.008],
                                 [7, 250998.008],
                                 [8, 184932.4201]]),
                       columns=['sensor', 'distance'])

cube375 = pd.DataFrame(np.array([[2, 251793.5662],
                                 [3, 375000],
                                 [4, 389422.6496],
                                 [5, 192743.3527],
                                 [6, 303768.0036],
                                 [7, 314085.9755],
                                 [8, 219146.07]]),
                       columns=['sensor', 'distance'])

cube400 = pd.DataFrame(np.array([[2, 354330.3543],
                                 [3, 450000],
                                 [4, 469813.7929],
                                 [5, 246475.1509],
                                 [6, 376497.0119],
                                 [7, 376497.0119],
                                 [8, 277398.6301]]),
                       columns=['sensor', 'distance'])

