import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

#title
st.title('VehicleData')
st.text('A web development demo powered by Streamlit')

#create text header
st.header('Vehicle Dataframe')

#display dataframe
st.dataframe(df)

st.title('Options')

#for handling the checkbox
hiding_outliers=True

df_cut = df[(df['price'] < 100000)].copy() #avoid SettingWithCopy warning later
df_used = df_cut
outlier_disclaimer = ' (priced under $100k)'

def handle_outliers():
    if hiding_outliers:
        hiding_outliers = False
        outlier_disclaimer = ''
        df_used = df
    else:
        hiding_outliers = True
        outlier_disclaimer = ' (priced under $100k)'
        df_used = df_cut

st.checkbox('Hide Cars Above $100,000 Asking Price', value=hiding_outliers, on_change=handle_outliers)

#Price histogram
st.header('Price Distribution')
fig1 = px.histogram(data_frame=df['price'], nbins=200, range_x=[0,100000],
             width=900, title='Price Distribution (All Cars Under $100k)',
             labels={
                 'value': 'Price (USD)',
                 'count': 'Number of cars'
             })
st.plotly_chart(fig1)

st.title('Price vs. Model Year scatter plot')
fig2 = px.scatter(data_frame=df_used, y='price', x='model_year', title='Price vs. Model Year' + outlier_disclaimer, opacity=0.3)
st.plotly_chart(fig2)

st.title('Price vs Condition scatter plot')
order_list = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']

fig3 = px.scatter(data_frame=df_cut, y='price', x='condition', title='Price vs. Condition' + outlier_disclaimer, opacity=0.3,
                 category_orders={'condition': order_list})
st.plotly_chart(fig3)