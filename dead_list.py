import requests
import pandas as pd
import streamlit as st
def dead_list():
    data = requests.get('https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4002')

    df = pd.read_json(data.text)
    rename_map ={"id":"ID","a01":"公布日","a02":"案號","a03":"性別","a04":"年齡","a05":"慢性病史","a06":"活動接觸史","a07":"發病日","a08":"症狀","a09":"採檢日","a10":"住院\/隔離日","a11":"確診日","a12":"死亡日"}
    df = df.rename(rename_map, axis=1)
    st.dataframe(df)
