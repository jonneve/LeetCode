import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    # Check theres sufficient rows in employee table to satisfy nth record retrieval, check for salary col protection as sort by will error if no col
    if (len(employee) < N) or ('salary' not in employee.columns):
        return pd.DataFrame(data=[pd.NA], columns=[f'getNthHighestSalary({N})'])

    # create new row using dense ranking, sorting in descending order    
    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False)
    
    # check there is n rank present
    if len(employee[employee['rank'] == N][['salary']]) == 0:
        return pd.DataFrame(data=[pd.NA], columns=[f'getNthHighestSalary({N})'])
    # return new df following expected formatting, where data is the Nth ranked highest salary item
    return pd.DataFrame(data=[employee[employee['rank'] == N]['salary'].drop_duplicates().item()], columns=[f'getNthHighestSalary({N})'])