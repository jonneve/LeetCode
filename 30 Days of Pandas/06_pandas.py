import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # create bonus col using lambda function (not modulo 2 will be true if odd, then use string slicing to check for M char)
    employees['bonus'] = employees.apply(lambda x: x['salary'] if (x['employee_id'] % 2 != 0) & (x['name'][0] != 'M') else 0, axis = 1)

    # return selected cols ordered by employee id
    return employees[['employee_id', 'bonus']].sort_values('employee_id')