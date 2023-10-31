import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    # data object using expected column names and accounts count using df masking to create a list data
    data = {'category':['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count':[len(accounts[accounts['income'] < 20000]), len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]), len(accounts[accounts['income'] > 50000])]}

    # return df as per expected format
    return pd.DataFrame(data)