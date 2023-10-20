import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # orders df merged with company to get company name
    orders_df = orders.merge(company, on = 'com_id', how='left')

    # find red sellers by checking company name is string 'red'
    red_sellers = orders_df[orders_df['name'].str.lower() == 'red']['sales_id'].tolist()

    # return names of non-red sellers using lambda function
    return sales_person[sales_person['sales_id'].apply(lambda x :x not in red_sellers)][['name']]