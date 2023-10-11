import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    # df mask tusing regex to check for first char being alphabetical, preffix then consists of alpha/digits/allowed special char of any length
    # then suffix is domain name
    mask = users['mail'].str.match(r'[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com')

    # return filtered df in unspecified order
    return users[mask]