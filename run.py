import gspread
from google.oauth2.service_account import Credentials
""" nur die KLasse (Credentials) aus der libary (google.oauth2.service_account) wird importiert """
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
""" Großgeschriebene Variabelen sind Konstante, die nicht verändert werden sollten """

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches') 
""" das ist der name vom EXCEL-file """

""" sales = SHEET.worksheet('sales') 
das ist eine sheet aus dem Ex-file

data = sales.get_all_values()
print(data) """

def get_sales_data():
    """
    Get sales figures import from user
    """
    while True:
        print('Plase enter sales data from the last market')
        print('Data shoud be six numbers, seperetated by commas')
        print('Example: 10, 20 ,30, 40 ,50, 60\n')

        data_str = input('Enter your data here: ')
        sales_data = data_str.split(',')

        if validate_data(sales_data):
            print('Data is valid!')
            break

    return sales_data

def validate_data(values):
    """
    converts values ti int, raises valueErrors 
    if not 6 numbers or vales can't be converted
    """
    try:
        [int(values) for values in values]
        if len(values) !=6:
            raise ValueError(
                f'Exactly 6 numbers! You provided {len(values)} numbers'
            )
    except ValueError as e:
        """ e wird zu variable """
        print(f'Invalid data: {e}! Please try again!\n')
        return False

    return True

""" def update_sales_worksheet(data):
    """
"""     update sales worksheet, add new row with the list data provided.
 """    """
    print('Updating sales worksheet.\n')
    sales_worksheet = SHEET.worksheet('sales')
    data from Ex-file - sales
    sales_worksheet.append_row(data)
    fügt eine Row ins worksheet hinzu
    print('Sales worksheet updated successfuly.\n')

def update_surplus_worksheet(data):
    """
"""     update surplus worksheet, add new row with the list data provided.
 """    """
    print('Updating surplus worksheet.\n')
    surplus_worksheet = SHEET.worksheet('surplus')
    data from Ex-file - surplus
    surplus_worksheet.append_row(data)
    fügt eine Row ins worksheet hinzu
    print('Surplus worksheet updated successfuly.\n') """

def update_worksheet(data, worksheet):
    """
    Gets a list of data and puts it into the worksheet.
    kombiniert die beiden vorherigen functions
    """
    print(f'Updating {worksheet} worksheet.\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfuly.\n')


def calculate_surplus_data(sales_row):
    """
    compares sales with stock and calculates suplus data
    """
    print('Calculate surplus data.../n')
    stock = SHEET.worksheet('stock').get_all_values()
    """ pprint(stock) """
    stock_row = stock[-1]
    """ 
    print(f'stock_row: {stock_row}')
    print(f'sales_row: {sales_row}') 
    """
    suplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        """ loop durch 2 lists gleichzeitig """
        surplus = int(stock) - sales
        suplus_data.append(surplus)

    return suplus_data

def get_last_5_entires_sales():
    """
    collects last 5 entries of data colloms of sandwiches
    """
    sales = SHEET.worksheet('sales')
    columns = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
        """ holt die letzten 5 """
    return columns

def calculate_stock_data(data):
    """
    calculate the average stoch for each item-type adding 10%
    """
    print('Calculating stock data...\n')
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column)/len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))
    return new_stock_data




def main():
    """
    run all functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    """ print(new_suplus_data) """
    update_worksheet(new_surplus_data, 'surplus')
    """ called die function and changes 'surplus'sheet in Ex tabelle """
    sales_columns = get_last_5_entires_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, 'stock')

print('Welcome to Love Sanwiches - Data Automation')
main()
