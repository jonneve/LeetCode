import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    # make new df after grouping by date id then make, aggregate lead id and partner id by number of unique count 
    df = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id' : ['nunique'], 'partner_id' : ['nunique']}).reset_index(col_level = 1)
    
    # formatting to ensure df meets expected return format 
    df.columns = df.columns.droplevel()
    df.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    return df