import pandas as pd
import wget
import glob


def load_df(asset, filename):
    data = pd.read_csv(filename, header=None, low_memory=False, dtype={
                       3: float}, usecols=[0, 1, 3], skiprows=2)

    for n, i in enumerate(data[1]):
        if i == asset:
            data = pd.DataFrame(data.values[n:])
            break

    for n, j in enumerate(data[1]):
        if j != asset:
            data = pd.DataFrame(data.values[:n])
            break

    del data[0]
    del data[1]
    return data


def load_dfs(asset, filenames):
    a = []
    first = True
    for i in filenames:
        data = load_df(asset, filename=i)
        if not first:
            a = pd.concat([a, data], ignore_index=True)
        else:
            first = False
            a = data
    return a
