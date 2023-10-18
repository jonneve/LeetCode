import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    # merge df's using a left join on the id col, return only select cols
    return employees.merge(employee_uni, on = 'id', how = 'left')[['unique_id', 'name']]