### Main page for streamlit resume
# from audioop import add
# from email import header
# import streamlit as st
# #import pages.Data_Visu_updated_excel_eplus_result
# import os
# import glob
# import pandas as pd
# import time
import streamlit as st
# import plotly.express as px
# from openpyxl import Workbook

st.set_page_config(
        page_title="Data Visulization for EnergyPlus Outputs",
        #page_icon=":sleuth_or_spy:",
	    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    )

st.sidebar.markdown('<a href="mailto:brijesh221097@gmail.com">Contact us !</a>', unsafe_allow_html=True)

# import pages.FileInputs
# import pages.CompareVariables
# import pages.DataAnalysis
# import pages.About
# def parse_energyplus_datetime_string(st, year=2021):
#     st=st.strip()
#     month=int(st[0:2])
#     day=int(st[3:5])
#     hour=int(st[7:9])
#     minute=int(st[10:12])
#     second=(st[13:15])
#     if not hour==24:
#         dt=pd.Timestamp(year,month,day,hour,minute)
#     else:
#         hour=0
#         dt=pd.Timestamp(year,month,day,hour,minute)
#         dt+=pd.Timedelta('1 day')
#     return dt


# def visulization():
#     #folder_location = "C:\\Users\\SetuBrije\\Desktop\\fil"

#     folder_location = st.text_input("Enter file's location ",help="Enter your file path",)
#     if len(folder_location) == 0:
#         st.text("Enter your file path! I am wating for it!!!")

#     if len(folder_location) != 0:
#         os.chdir(folder_location)
#         extension = 'csv'
#         all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#         st.write("Files available are: ",all_filenames)
#         dest_wb = Workbook()
            
#         combined_csv = pd.concat({f: pd.read_csv(f, encoding='unicode_escape', sep=',',parse_dates=[0],
#                index_col=[0],date_parser=parse_energyplus_datetime_string )
#                 for f in all_filenames}, axis=1)
    
#         df = combined_csv.T
#         df.index = df.index.map('_'.join)
#         df = df.T
#         x=df.index
#         # for i in df.columns:
#         #     if "Date" in i:
#         #         df = df.drop(i, axis=1)
#         df = df.T.drop_duplicates().T
#         columnlist = df.columns
#         k=1
#         return df,x,columnlist,k
        # st.write("Total Parameters available:" + str(len(columnlist)))
        # form = st.form("my_form")
        # dropdown = form.multiselect("Enter variable of csv files: ",columnlist)
        # submitted =form.form_submit_button("Submit")
        
        # if submitted:
        #     with st.spinner('Wait for it...'):
        #         my_bar = st.progress(0)
        #         for percent_complete in range(100):
        #             time.sleep(0.1)
        #             my_bar.progress(percent_complete + 1)
        #         #time.sleep(5)
        #     st.success('Done!')
            

        #     #x=df.columns[0]
        #     y=dropdown
        #     fig = px.line(df, x=x, y=y, title='Energy meter time series chart')
        #     fig.update_layout(legend=dict(
        #         orientation="h",
        #         yanchor="bottom",
        #         y=1.02,
        #         xanchor="right",
        #         x=1
        #     ))
            
        #     st.plotly_chart(fig, use_container_width=True)

#tabs= st.tabs(["Choose a Page","Introduction", "Data Visualization", "About"])
# add_selectbox = st.sidebar.selectbox(
#     "Select one page",
#     ("Introduction", "Data Visualization","Data Analysis" ,"About")
# )

# if add_selectbox == "Introduction":
st.title("Introduction about tool")
st.text("Brijesh Jasani")
st.subheader("Step-1: Create and run EnergyPlus simulation")
st.markdown(" - Create EnergyPlus model or idf file using EnergyPlus/Eppy")
st.markdown(" - Run EnergyPlus simulation with **readvars=True**")
st.markdown(" - For more information explore following resourses: [EnergyPlus Essentials](https://energyplus.net/assets/nrel_custom/pdfs/pdfs_v9.5.0/EnergyPlusEssentials.pdf)[Chapter 3],[bigladder software](https://bigladdersoftware.com/epx/docs/8-0/input-output-reference/page-090.html) ")
st.subheader("step-2: Add your all coma seperated csv files into one folder")
st.markdown(" - After Running EnergyPlus simulation with **readvars=True**, it will automatically generates ***comma seperated file*** which contains all the available variables (max.255 variables)")
st.markdown("- Rename file name and add into one folder, repeat the same thing for all the cases")
st.subheader("step3: Enter file location in app")
st.markdown("- Add your folder path in this app")
st.subheader("step4: Select/search variables for data visualization")
st.markdown("- Use ***Variable Compare*** option for compare varibles from diffrent files/cases")
st.markdown("- Use ***Data Exploration*** option for understand basic features of available data columns")
st.markdown("- For ex. variation in data, correlation")
st.subheader("step5: done! Enjoy!!")


# if add_selectbox == "Data Visualization":
#     outputs = visulization()
    
#     df = outputs[0]
#     x = outputs[1]
#     columnlist= outputs[2]
#     st.write("Total Parameters available:" + str(len(columnlist)))
#     form = st.form("my_form")

#     dropdown = form.multiselect("Enter variable of csv files: ",columnlist)
#     submitted =form.form_submit_button("Submit")
    
#     if submitted:
#         with st.spinner('Wait for it...'):
#             my_bar = st.progress(0)
#             for percent_complete in range(100):
#                 time.sleep(0.1)
#                 my_bar.progress(percent_complete + 1)
#             #time.sleep(5)
#         st.success('Done!')

#         y=dropdown
#         fig = px.line(df, x=x, y=y, title='Energy meter time series chart')
#         fig.update_layout(legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ))
        
#         st.plotly_chart(fig, use_container_width=True)


# if add_selectbox == "Data Analysis":
#     outputs = visulization()
#     df = outputs[0]
#     x = outputs[1]
#     columnlist= outputs[2]
#     #folder_location = "C:\\Users\\SetuBrije\\Desktop\\fil"
#     st.write("Total Parameters available:" + str(len(columnlist)))
#     form = st.form("my_form")

#     dropdown = form.multiselect("Enter variable of csv files for analysis: ",columnlist)
#     submitted =form.form_submit_button("Submit")
    
#     if submitted:
#         with st.spinner('Wait for it...'):
#             my_bar = st.progress(0)
#             for percent_complete in range(100):
#                 time.sleep(0.1)
#                 my_bar.progress(percent_complete + 1)
#             #time.sleep(5)
#         st.success('Done!')
        

#         #x=df.columns[0]
#         y=dropdown
#         fig = px.histogram(df,  y=y, title='Histogram')
#         fig.update_layout(legend=dict(
#             orientation="v",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ))
        
#         st.plotly_chart(fig, use_container_width=True)
#         fig1 = px.box(df,  y=y, title='Box plot of selected variables',width=1000,height=700)
#         fig1.update_layout(legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ))
#         st.plotly_chart(fig1, use_container_width=True)



#         corr_para = st.selectbox("Select parameter for corelation calculations", columnlist)
#         df_corr = df.corr()
#         df_corr_1 = pd.DataFrame(df_corr.loc[:,corr_para]).sort_values(by=corr_para,ascending=False)
#         df_corr_2 = pd.DataFrame(df_corr.loc[:,corr_para]).sort_values(by=corr_para)
#         #number=st.slider('Number of bars', 5,10,5)
#         st.write(df_corr_1.head())
#         st.write(df_corr_2.head())



        #col1,col2 = st.columns(2)
        #fig2 = px.bar(df_corr_1.head(number))
        #col1.plotly_chart(fig2, use_container_width=True)

        #fig3 = px.bar(df_corr_2.head(number))
        #col2.plotly_chart(fig3, use_container_width=True)
        # y_df = df[y].describe()

        # for j  in y_df.columns:
        #     st.subheader(j)
        #     col1, col2, col3 = st.columns(3)
        #     for i in range (0,len(y_df.columns)):
                #col1.metric("Count", round(y_df.iloc[:,i][0],2))
                # col2.metric("", "9 mph", "-8%")
                # col3.metric("Humidity", "86%", "4%")
# delta=-0.5,
#         delta_color="inverse"

 



# if add_selectbox == "About":
#     st.title("About")
#     st.markdown(" Do you like this app?")
#     st.markdown(" Any suggestions?")
#     st.write(" Please give your feedback here [Gmail](brijesh221097@gmail.com)")
#     st.write("\U0001F4E1 you can contact me here \U0001F603	,[LinkedIn](https://www.linkedin.com/in/brijesh-jasani/),   ")
















