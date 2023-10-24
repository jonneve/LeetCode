import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    # create new row using dense ranking, sorting in descending order 
    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False)
        
     # check there is a 2nd highest salary present
    if len(employee[employee['rank'] == 2][['salary']]) == 0:
        return pd.DataFrame(data=[pd.NA], columns=['SecondHighestSalary'])
    # return new df following expected formatting, where data is the 2nd ranked highest salary item
    return pd.DataFrame(data=[employee[employee['rank'] == 2]['salary'].drop_duplicates().item()], columns=['SecondHighestSalary'])