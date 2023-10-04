import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    # data mask with area OR population conditions
    mask = (world['area'] >= 3000000) | (world['population'] >= 25000000)
    # cols to be returned
    cols = ['name', 'population', 'area']

    return world[mask][cols]