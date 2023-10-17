import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    # group by sell date and aggregate on the product series
    # num_sold column is lambda function finding unique count
    # products col is the product list elements joined with a comma after sorting 
    return activities.groupby('sell_date')['product'].agg([('num_sold', lambda x: x.nunique()), ('products', lambda x: ','.join(sorted(x.unique())))]).reset_index()