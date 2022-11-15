import gspread
from google.oauth2.service_account import Credentials
""" nur die KLasse (Credentials) aus der libary (google.oauth2.service_account) wird importiert """

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
    print('Plase enter sales data from the last market')
    print('Data shoud be six numbers, seperetated by commas')
    print('Example: 10, 20 ,30, 40 ,50, 60\n')

    data_str = input('Enter your data here: ')
    print(f'The data prvided is: {data_str}')

get_sales_data()
