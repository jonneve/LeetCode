import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    # safety check to ensure at least 1 row of order data
    if len(orders) < 1:
        return pd.DataFrame(data = None, columns= ['customer_number'])
        
    # get df grouped by count of orders per customer
    df = orders.groupby('customer_number').count().reset_index()

    # retrun single col as a df after filtering by index of row with max order number
    return df.loc[[df['order_number'].idxmax()]][['customer_number']]