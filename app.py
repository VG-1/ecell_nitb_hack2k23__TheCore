import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.button('Log In')
# st.header(')

i = ('WhatsApp Image 2023-02-12 at 20.05.59.jpg')
# st.image(image='WhatsApp Image 2023-02-12 at 20.05.59.jpg')
# st.image(i,width=555,use_column_width=500,output_format='auto')
col1, col2, col3 = st.columns(3)


with col1,col2:
    st.image("WhatsApp Image 2023-02-12 at 20.05.59.jpg",width=550)
with col3:
    st.write('          ')

# st.subheader('Hope we are helpful to you 🙌')
st.markdown("<h1 style='text-align: center; color: white;'>Here is the shining statisitics of our placements😍</h1>", unsafe_allow_html=True)

excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'
df = pd.read_excel(excel_file,sheet_name=sheet_name,usecols='B:D',header=3)
df_participants = pd.read_excel(excel_file,sheet_name= sheet_name,usecols='F:G',header=3)
df_participants.dropna(inplace=True)

company = df['Company'].unique().tolist()
ages = df['Year'].unique().tolist()
age_selection = st.slider('Year:', min_value= min(ages), max_value= max(ages), value=(min(ages),max(ages)))
company_selection = st.multiselect('Company:',company, default=company)

mask = (df['Year'].between(*age_selection)) & (df['Company'].isin(company_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

df_grouped = df[mask].groupby(by=['Job_Role']).count()[['Year']]
df_grouped = df_grouped.rename(columns={'Year': 'Placed_Students'})
df_grouped = df_grouped.reset_index()

st.title('Companies visited past years')
col1, col2 = st.columns(2)
with col1:
        bar_chart = px.bar(df_grouped,x='Job_Role',y='Placed_Students',text='Placed_Students',color_discrete_sequence = ['#F63366']*len(df_grouped),template= 'plotly_white')
        st.plotly_chart(bar_chart)


st.title('Companies visited past years')
col1, col2, col3 = st.columns(3)
with col1:
        st.write(' ')
with col2:
        st.dataframe(df[mask])
with col3:
        st.write(' ')
st.title('Most candidates hired by company in percentage')
pie_chart = px.pie(df_participants,values='Participants', names='Companies')
st.plotly_chart(pie_chart)
