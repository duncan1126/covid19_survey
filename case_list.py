import requests
import pandas as pd
import streamlit as st
def case_list():
    data = requests.get('https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4003')

    df = pd.read_json(data.text)
    rename_map ={"id":"","a01":"通報日","a02":"法定傳染病通報","a03":"居家檢疫送驗","a04":"擴大監測送驗","a05":"送驗(今日合計)","a06":"送驗(總累計)","a07":"排除(總累計)","a08":"昨日排除","a09":"昨日送驗"}
    df = df.rename(rename_map, axis=1)
    st.dataframe(df)
