from persistence import *

def print_table_by_selected_order(table, order):
    print(table._table_name.capitalize())
    for record in table.find_all_in_selected_order(order):
        print(record)


def print_employees_report():
    print('Employees report')
    employees_report_curs = repo._conn.cursor()
    stmt = '''
        SELECT employees.name, employees.salary, branches.location, IFNULL(SUM(ABS(activities.quantity) * products.price),'0')
        FROM employees 
        JOIN branches ON employees.branche = branches.id
        LEFT JOIN activities ON activities.activator_id = employees.id 
        LEFT JOIN products ON activities.product_id = products.id
        GROUP BY employees.id
        ORDER BY employees.name   
    '''
    employees_report_curs.execute(stmt)
    for employe_report in employees_report_curs:
        print(*employe_report, sep=' ')
    
def print_activities_report():
    print('Activities report')
    activity_reports_curs = repo._conn.cursor()
    stmt = """SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name 
    FROM activities 
    JOIN products ON activities.product_id = products.id
    LEFT JOIN suppliers ON activities.activator_id = suppliers.id AND suppliers.id IS NOT NULL
    LEFT JOIN employees ON activities.activator_id = employees.id AND employees.id IS NOT NULL
    ORDER BY activities.date
    """
    activity_reports_curs.execute(stmt)
    for activity_report in activity_reports_curs:
        print(activity_report)
    

def main():
    #TODO: implement
    print_table_by_selected_order(repo.activities, 'date')
    print_table_by_selected_order(repo.branches, 'id')
    print_table_by_selected_order(repo.employees, 'id')
    print_table_by_selected_order(repo.products, 'id')
    print_table_by_selected_order(repo.suppliers, 'id')
    print('')
    print_employees_report()
    print('')
    print_activities_report()
    

if __name__ == '__main__':
    main()