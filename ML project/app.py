import streamlit as st
import pickle

st.title("Laptop Predict")

pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('df.pkl','rb'))

#brand

company = st.selectbox('Brand',data['Company'].unique())

#type of laptop

type= st.selectbox('Type',data['TypeName'].unique())

#Ram

Ram =st.selectbox('Ram(in GB)' , data['Ram'].unique())

#Weight

Weight = st.number_input('Weight')

#TouchScreen

touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

#Ips

ips = st.selectbox('Ips Display', ['No','Yes'])

#screen_size

screensize = st.number_input('Screen Size')

#resolution

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu

cpu = st.selectbox('CPU',data['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',data['Gpu brand'].unique())

os = st.selectbox('OS',data['os'].unique())

if st.button('Predict Price'):
    pass