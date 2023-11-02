import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # group manager ids by count of managed employees
    managed_count = employee.groupby('managerId').count().reset_index()

    # lamda function to show true if managed count >= 5, then use this as a mask to filter df
    # retrun expected df format showing just manager name if theres one or more applicable managers
    if len(managed_count[managed_count['id'] >= 5]['managerId'].to_list()) >= 1:
        return employee[employee.apply(lambda x: x['id'] in managed_count[managed_count['id'] >= 5]['managerId'].to_list(), axis = 1)][['name']]
    else:
        return pd.DataFrame(data=[], columns=['name'])