import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # merge two dfs and create a max salary col ffor mask filtering using max argument
    merge_df = employee.merge(department, left_on = 'departmentId', right_on ='id', how = 'left')
    max_salary = merge_df.groupby('name_y')['salary'].transform('max')

    # use max salary to filter merge df to only show rows with max salaries, reformat as per expected return df
    df = merge_df[merge_df['salary'] == max_salary][['name_y', 'name_x', 'salary']]
    df.columns = ['Department', 'Employee', 'Salary']

    return df