import os
import glob
import pandas as pd
import time
import streamlit as st
import plotly.express as px
from openpyxl import Workbook



def parse_energyplus_datetime_string(st, year=2021):
    st=st.strip()
    month=int(st[0:2])
    day=int(st[3:5])
    hour=int(st[7:9])
    minute=int(st[10:12])
    second=(st[13:15])
    if not hour==24:
        dt=pd.Timestamp(year,month,day,hour,minute)
    else:
        hour=0
        dt=pd.Timestamp(year,month,day,hour,minute)
        dt+=pd.Timedelta('1 day')
    return dt

def main():
    #folder_location = "C:\\Users\\SetuBrije\\Desktop\\fil"
    folder_location = st.text_input("Enter files location ",)
    if len(folder_location) != 0:
        os.chdir(folder_location)
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        st.write("Files available are: ")
        for i in all_filenames:
            st.write(i)
        
        dest_wb = Workbook()
            
        combined_csv = pd.concat({f: pd.read_csv(f, encoding='unicode_escape', sep=',',parse_dates=[0],
                index_col=[0],date_parser=parse_energyplus_datetime_string )
                    for f in all_filenames}, axis=1)

        df = combined_csv.T
        df.index = df.index.map('_'.join)
        df = df.T
        st.write("Total variables available: ",len(df.columns))
        x=df.index
        df_duplicate = df.T.drop_duplicates().T
        st.write("Identical columns found:", (len(df.columns)-len(df_duplicate.columns)))
        columnlist = df.columns
        k=1
        return (df,x,columnlist)
    
def visu():
    form = st.form("my_form")
    dropdown = form.multiselect("Enter variable of csv files: ",columnlist)
    submitted =form.form_submit_button("Submit")

    if submitted:
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)

        y=dropdown
        fig = px.line(df, x=x, y=y, title='Energy meter time series chart')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        
        st.plotly_chart(fig, use_container_width=True)

if __name__== "__main__" :
    var=main()
    if var:
        df=var[0]
        x=var[1]
        columnlist = var[2]
        visuli=visu()
