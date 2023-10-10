import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # lambda funtion to apply capitalize case formatting 
    users['name'] = users.apply(lambda x: x['name'].capitalize(), axis = 1)

    # return df ordered by user id
    return users.sort_values('user_id')