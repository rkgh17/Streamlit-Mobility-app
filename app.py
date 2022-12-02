# -*- coding: utf-8 -*-

import streamlit as st
import sys
sys.path.insert(1, "C:\Users\h\Desktop\ToyProject\Streamlit-Mobility-app\venv\Lib\site-packages\streamlit_option_menu")
from streamlit_option_menu import option_menu
from pathlib import Path

def main():

    with st.sidebar:
        selected = option_menu(None, ["Home", 'Settings'], 
        icons=['house', 'gear'], 
        menu_icon="list", 
        default_index=1, 
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#B8FFAA"},
        "nav-link-selected": {"font-size":"20px","background-color": "PaleGreen", "color":"black"},
        })
        # print(selected)
    
    if selected == "Home":
        home = Path("md/home.md").read_text(encoding='UTF-8')
        st.markdown(home, unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()