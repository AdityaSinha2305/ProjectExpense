# WELCOME TO PROJECT EXPENSE

import pandas as pd

df = pd.read_excel("Expense2024.xlsx")

# month = input("Enter the month name you want to find the expense: ")
# month_name = month.capitalize()

# df = df[df['Month']==month_name]

def expense(df,months_data_df):
    next_month = True    
    while(next_month):
        print()
        month = input("Enter the month name you want to find the expense: ")
        month_name = month.capitalize()

        month_df = df[df['Month']==month_name]


        print(f"-------- {month_name.upper()} Expense Analysis -------------")
        print()

        # Total Amount spend in the month of November using online and cash both.
        df_total = month_df['Amount'].sum()
        print(f'Actual total amount spend is "{df_total}"')

        print()

        # Total amount spend in the month of November using online (Sb and Cb)
        df_online = month_df.loc[(month_df['Payment Mode']=='Online(SBI)') | (month_df['Payment Mode']=='Online(CBI)') , 'Amount'].sum()

        print(f'Total Amount spend using online is {df_online}')


        # Total amount spend in the month of November using cash
        df_cash = month_df.loc[ month_df['Payment Mode']=='Cash' , 'Amount'].sum()
        print(f'Total Amount spend using cash is {df_cash}')


        print()


        # Total amount spend in the month of November using online Cb
        df_cb_online = month_df.loc[month_df['Payment Mode']=='Online(CBI)' , 'Amount'].sum()
        print(f'Total Amount spend using online cb is {df_cb_online}')


        # Total amount spend in the month of November using online Cb
        df_sb_online = month_df.loc[month_df['Payment Mode']=='Online(SBI)' , 'Amount'].sum()
        print(f'Total Amount spend using online sb is {df_sb_online}')

        print()


        print("**Category Wise Expense Analysis**")
        print()

        # 1.  Total Amount spent on Food  (Note: 'month_df' is the dataframe for that particular month only)
        df_food = month_df.loc[ month_df['Category']=='Food' , 'Amount'].sum()
        print('Total Amount spent on Food is :',df_food)


        # 2.  Total Amount spent on Grocery  (Note: 'month_df' is the dataframe for that particular month only)
        df_grocery = month_df.loc[ month_df['Category']=='Grocery' , 'Amount'].sum()
        print('Total Amount spent on Grocery is :',df_grocery)

        # 3.  Total Amount spent on Grocery  (Note: 'month_df' is the dataframe for that particular month only)
        df_travel = month_df.loc[ month_df['Category']=='Travel' , 'Amount'].sum()
        print('Total Amount spent on Travel is :',df_travel)

        # 4.  Total Amount spent on Other  (Note: 'month_df' is the dataframe for that particular month only)
        df_other = month_df.loc[ month_df['Category']=='Other' , 'Amount'].sum()
        print('Total Amount spent on Other is :',df_other)

        print()

        print("---------------------------------------------------------")

        # Creating a new dataframe for all the values
        data = {
            'Month': [month_name], 
            'Total': [df_total],
            'Online': [df_online],
            'Cash': [df_cash],
            'CBI': [df_cb_online],
            'SBI': [df_sb_online],
            'Food': [df_food],
            'Grocery': [df_grocery],
            'Travel': [df_travel],
            'Other': [df_other]
            }

        new_row = pd.DataFrame(data)

        # To add new row in dataframe
        months_data_df = months_data_df._append(new_row, ignore_index=True)
        # print(months_data_df)
        print()

        next_month = input('Do you want to add expense detail of next month as well ? Press Y or N: ')
        if next_month.upper()=='Y':
            next_month = True
        else:
            next_month = False
    
    return months_data_df


def display_month_data(final_month_data_df):
    print("===============================================================================")
    print(final_month_data_df)
    print("===============================================================================")


def export(final_month_data_df):

    # index=False means default index of dataframe is not stored in excel sheet
    final_month_data_df.to_excel(f'Month_wise_expense.xlsx', index=False)
    print("Month sheet exported successfully. You can now safely close this program")
    print()


if __name__=="__main__":
    
    months_data_df = pd.DataFrame()         # An empty dataframe is used to store results of each month as a row
    
    # months_data_df is passed for an empty dataframe so that new row will add upon for each month
    final_month_data_df = expense(df,months_data_df)
    
    display_month_data(final_month_data_df)

    print()

    export(final_month_data_df)