import requests
import pandas as pd
import streamlit as st
def tw_recode():
    data = requests.get('https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4001&limited=TWN')

    df = pd.read_json(data.text)
    rename_map ={"id":"ID","a01":"iso_code","a02":"洲名","a03":"國家","a04":"日期","a05":"總確診數","a06":"新增確診數","a07":"七天移動平均新增確診數","a08":"總死亡數","a09":"新增死亡數","a10":"七天移動平均新增死亡數","a11":"每百萬人確診數","a12":"每百萬人死亡數","a13":"傳染率","a14":"新增檢驗件數","a15":"總檢驗件數","a16":"每千人檢驗件數","a17":"七天移動平均新增檢驗件數","a18":"陽性率","a19":"每確診案例相對檢驗數量","a20":"疫苗總接種總劑數","a21":"疫苗總接種人數","a22":"疫苗新增接種劑數","a23":"七天移動平均疫苗新增接種劑數","a24":"每百人接種疫苗劑數","a25":"每百人接種疫苗人數","a26":"疫情控管指數","a27":"總人口數","a28":"中位數年紀","a29":"70歲以上人口比例","a30":"平均壽命","a31":"解除隔離數","a32":"解封指數"}
    df = df.rename(rename_map, axis=1)
    st.dataframe(df)


