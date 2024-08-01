import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st
st.header('WEEKS REPORT ON REVENUE COLLECTED')
st.sidebar.subheader('TEAMS PERFORMANCE')
df=pd.read_csv('Revenue compliance.csv')
x=df['TEAMS']
y=df['TOTALS']
bar=plt.bar(x,y,color='blue')
plt.xlabel('TEAMS')
plt.ylabel('TOTALS')
st.dataframe(df)
st.pyplot()
hist=plt.hist(y,bins=2)
plt.ylabel('TEAMS')
st.dataframe(df)
st.pyplot()
scatter=alt.Chart(df).mark_circle().encode(
    x='TEAMS',
    y='TOTALS',
    color='TEAMS',
    tooltip=['27/05/2024','28/05/2024','29/05/2024','30/05/2024','31/05/2024','3/6/2024','4/6/2024','5/6/2024','6/6/2024','7/6/2024']
).properties(
    title='THIS IS A SCATTERPLOT OF DATA',
    width=600,
    height=400
).interactive()
st.dataframe(df)
st.altair_chart(scatter)
bar=alt.Chart(df).mark_bar().encode(
    x='TEAMS',
    y='TOTALS',
    color='TEAMS'
).properties(
    title='THIS IS A BARGRAPH ON TEAM PERFORMANCE',
    width=600,
    height=400
).interactive()
st.dataframe(df)
st.altair_chart(bar)




