import pandas as pd
import time
import streamlit as st
import plotly.express as px
from pages.FileInputs import main,parse_energyplus_datetime_string
from statsmodels.tsa.seasonal import seasonal_decompose
#folder_location = "C:\\Users\\SetuBrije\\Desktop\\fil"

var=main()

if var:
    tab1,tab2,tab3= st.tabs([ "Data Visualization", "Correlation","Custom Plot"])
    with tab1:
        df=var[0]
        columnlist = var[2]
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
            fig = px.histogram(df,  y=y, title='Histogram')
            fig.update_layout(legend=dict(
                orientation="v",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ))
            
            st.plotly_chart(fig, use_container_width=True)
            fig1 = px.box(df,  y=y, title='Box plot of selected variables',width=1000,height=700)
            fig1.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ))
            st.plotly_chart(fig1, use_container_width=True)
            
            # fig3 = px.line_polar(df, r=y, 
            #          line_close=True, 
            #         title='Polar seasonal plot',
            #         width=600, height=500)
            # st.plotly_chart(fig3, use_container_width=True)
            

    with tab2:

        x=df.index
        df = df.T.drop_duplicates().T
        columnlist = df.columns
        st.write('Great!')
        corr_para = st.selectbox("Select parameter for corelation calculations", columnlist)
        df_corr = df.corr()
        df_corr_1 = pd.DataFrame(df_corr.loc[:,corr_para]).sort_values(by=corr_para,ascending=False)
        df_corr_2 = pd.DataFrame(df_corr.loc[:,corr_para]).sort_values(by=corr_para)
        st.write(df_corr_1.head())
        st.write(df_corr_2.head())

    with tab3:
        x=st.selectbox("Select x- Component of graph",columnlist)
        y=st.selectbox("Select y- Component of graph",columnlist)
        z=st.selectbox("Select colour based on",columnlist)
        fig2 = px.scatter(df,x=x,  y=y, color=z, title='Scatter plot of selected variables')
        # fig2.update_layout(legend=dict(
        #     orientation="h",
        #     yanchor="bottom",
        #     y=1.02,
        #     xanchor="right",
        #     x=1
        # ))
        st.plotly_chart(fig2, use_container_width=True)



