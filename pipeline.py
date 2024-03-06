import pandas as pd

csv_file_path = "Data.csv"

df = pd.read_csv(csv_file_path)

selected_columns = [
    'Frame Colour',
    'Frame Surface',
    'Frame Material',
    'Glazing Type',
    'Size Horizontal [m]',
    'Size Vertical [m]',
    'Frame Depth [cm]'
]


df = df[selected_columns]

print(df.head())
