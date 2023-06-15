import pandas as pd
import streamlit as st
import datetime

st.set_page_config(page_title='CENTRAL REGISTRAR FOR COOPERATIVE SOCIETIES',
                   layout='wide')


df = pd.read_excel(
    io='dum_data.xlsx',
    engine='openpyxl',
    sheet_name='com_data',
    usecols='A:I',
    nrows=101,
    dtype={'Year':str}
)

df["Date"] = [
        datetime.datetime.strptime(
            str(target_date).split(" ")[0], '%Y-%m-%d').date()
        for target_date in df["Date"]
    ]

###buttons 

def create_button(url, label):
    return f'<a href="{url}"><button style="background-color: Red; border: 1px solid red; border-radius: 3px; padding: 2px 4px;">{label}</button></a>'


# Create a table with 1 row and 4 columns
col1, col2, col3, col4 = st.columns(4)

# Button 1
url1 = " https://godxanubis80085-dash01-df-app-6uqxb3.streamlit.app/ "
button_label1 = " Home  "
col1.markdown(create_button(url1, button_label1), unsafe_allow_html=True)

# Button 2
url2 = " https://godxanubis80085-dash01-df2-f63416.streamlit.app/ "
button_label2 = " Custom search "
col2.markdown(create_button(url2, button_label2), unsafe_allow_html=True)

# Button 3
url3 = "https://example.com/"
button_label3 = " Sorted View "
col3.markdown(create_button(url3, button_label3), unsafe_allow_html=True)

# Button 4
url4 = "https://example.com/"
button_label4 = " Trends "
col4.markdown(create_button(url4, button_label4), unsafe_allow_html=True)

###Main page 

st.title(" List of Registered Societies")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

#st.table(df)

########################## data limiter   ##############################

# Set the number of rows per page
rows_per_page = 10

# Get the total number of rows in the DataFrame
total_rows = len(df)

# Create a section for rows per page
rows_per_page = st.number_input("Rows per page:", min_value=1, max_value=total_rows, value=rows_per_page)

# Create a section for current page
current_page = st.number_input("Current page:", min_value=1, max_value=(total_rows // rows_per_page) + 1, value=1)

# Calculate the starting and ending indices for the current page
start_index = (current_page - 1) * rows_per_page
end_index = min(start_index + rows_per_page, total_rows)

# Slice the DataFrame to display only the rows for the current page
page_df = df[start_index:end_index]

# Display the table
st.table(page_df)

# Create a horizontal line separator
st.markdown("---")

# Display the current page  at the bottom of the 
page_start = start_index + 1
page_end = min(start_index + rows_per_page, total_rows)
st.write(f"Showing {page_start} - {page_end} of {total_rows} | Current Page: {current_page}")







