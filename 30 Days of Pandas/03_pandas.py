import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # merge the two df's then provider indicator to show which are only present in left (cutsomer) table and not order table
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='outer', indicator=True)
    ans = merged[merged['_merge'] == 'left_only'][['name']]
    # change result format
    ans.columns = ['customers']
    
    return ans