from __future__ import print_function
import pprint
import pandas as pd
from gspread_pandas import Spread, Client, conf


conf.get_config("auth_secret/google_secret.json")

# Print nicely
pp = pprint.PrettyPrinter()

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
id_sheetname = "20SH07 Food ID Map"
spread = Spread(id_sheetname)
id_df = spread.sheet_to_df()

column_map = {
    "ID": 1,
    "Exact_Name": 2,
    "Recess": 3,
    "Lunch": 4,
    "Price": 5,
    "Name": 6,
    "MON/TUE/WED/TURS/FRI": 7,
    "Stall": 8
}

stall_map = {
    "Stall 1  Fried Hokkien Mee": 1,
    "Stall 2 Chicken Rice": 2,
    "Stall 3 Yong Tau Foo": 3,
    "Stall 4 WESTERN FOOD": 4,
    "Stall 5 Snacks": 5,
    "Stall 6 Hot Drink": 6,
    "Stall 7 Cold Drink": 7,
    "Stall 8 Chinese Set": 8,
    "Stall 9 Chinese Noodle": 9,
    "Stall 10 Japanese Food": 10,
    "Stall 11 Malay Food": 11,
    "Stall 12 PRATA HUT": 12
}

stall_number = len(stall_map)  # 12


def stall_to_func(n):
    """Switch-case statement to convert nth stall to their respect function containing stall specfic parsing code"""
    switcher = {
        1: stall1,
        2: stall2,
        3: stall3,
        4: stall4,
        5: stall5,
        6: stall6,
        7: stall7,
        8: stall8,
        9: stall9,
        10: stall10,
        11: stall11,
        12: stall12
    }
    # Get the function from switcher dictionary
    func = switcher.get(n, lambda: (
        _ for _ in ()).throw(Exception('Invalid Input')))
    # Execute and return the function
    return func()


def stall1():
    pass


def stall2():
    pass


def stall3():
    pass


def stall4():
    pass


def stall5():
    pass


def stall6():
    pass


def stall7():
    pass


def stall8():
    pass


def stall9():
    pass


def stall10():
    pass


def stall11():
    pass


def stall12():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
