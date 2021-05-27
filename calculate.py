import sys
import pandas as pd
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

try:
    df = pd.read_csv(sys.argv[1], index_col=0)
except IOError:
    print("Error opening file: ", sys.argv[1])
    sys.exit()

print(df)
df_result = pd.DataFrame(columns=['arrival_time', 'velocity', 'distance', 'channel'])

