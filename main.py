import streamlit as st
from dead_list import *
from case_list import *
from tw_recode import *
class into():
    def main():

        st.set_page_config(page_title='🎈 台灣疫情', layout='wide')
        st.title(f'台灣Covid-19疫情狀況')


    def sidebar():
        st.sidebar.title('報表')
        select = st.sidebar.radio('select',['recode','dead','case'])

        if select =='recode':
            tw_recode()
        elif select =='case':
            case_list()
        elif select =='dead':
            dead_list()
        elif select =='dead':
            dead_list()




# def read_csv():
#     url = 'https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv'
#     file = open(url, 'r', encoding='uft-8')
#     content = file.read()
#     file.close()
#     st.write(content)

if __name__ == '__main__':
    into.main()
    into.sidebar()

