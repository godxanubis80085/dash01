import pandas as pd
import streamlit as st
import plotly.express as px
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

###Main page 

st.title(" Custom Search")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

#city based 
state = st.sidebar.multiselect('Select the state : ' , 
                               options=df["State"].unique() 
                               )

#sector based 
sector = st.sidebar.multiselect('Select the Sector : ' , 
                               options=df["Sector_Type"].unique()
                               )

#year based 
year = st.sidebar.multiselect('Select the Year : ' , 
                               options=list(df["Year"].unique())
                                )

if state or sector or year:
    df_selection = df.query("State.isin(@state) & Sector_Type.isin(@sector) & Year.isin(@year)")
else:
    df_selection = df  # No filters applied, show the entire DataFrame

st.table(df_selection)

###################

