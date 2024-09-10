import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

#version of the chart with outlier prices removed
df_cut = df[(df['price'] < 100000)].copy() #avoid SettingWithCopy warning later

#generate charts

outlier_disclaimer = ' (priced under $100k)'

fig_hist = px.histogram(data_frame=df['price'], nbins=400,
             width=900, title='Price Distribution' + outlier_disclaimer,
             labels={
                 'value': 'Price (USD)',
                 'count': 'Number of cars'
             })

fig_year = px.scatter(data_frame=df, y='price', x='model_year', title='Price vs. Model Year' + outlier_disclaimer, opacity=0.3)

order_list = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']
fig_cond = px.scatter(data_frame=df, y='price', x='condition', title='Price vs. Condition' + outlier_disclaimer, opacity=0.3,
                 category_orders={'condition': order_list})

#title
st.title('VehicleData')
st.text('A web development demo powered by Streamlit')

#create text header
st.header('Vehicle Dataframe')

#display dataframe
st.dataframe(df)

st.title('Options')

hide_outliers = st.checkbox('Hide Cars Above $100,000 Asking Price', value=False)

if hide_outliers:
    fig_hist.data[0].update(x=df_cut['price'], nbinsx=100) #keeps bin size constant between modes
    fig_year.data[0].update(x=df_cut['model_year'], y=df_cut['price'])
    fig_cond.data[0].update(x=df_cut['condition'], y=df_cut['price'])


#Price histogram
st.header('Price Distribution')
st.plotly_chart(fig_hist)

st.title('Price vs. Model Year scatter plot')
st.plotly_chart(fig_year)

st.title('Price vs Condition scatter plot')
st.plotly_chart(fig_cond)