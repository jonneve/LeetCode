import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    # total_time calculated column by subtracting in from out
    employees['total_time'] = employees['out_time'] - employees['in_time']

    # group by id and day, where the aggregation is a sum of total time and reset index so grouping cols are not new multi-index
    df = employees.groupby(['event_day', 'emp_id']).sum().reset_index()[['event_day', 'emp_id', 'total_time']]
    
    # rename cols as per expected format 
    df.rename(columns = {'event_day':'day'}, inplace=True)

    return df