# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

import pandas as pd
import pydeck as pdk
import streamlit as st

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import streamlit as st
    st.title('My first app  111')
    st.write("""
                #My app
                Hello *world!*/n
                ##l;skjgirnigs
            """)

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    df = pd.DataFrame(
        np.random.randn(100, 2) / [0.5, 0.5] + [55.5, 37.33],
        columns=['lat', 'lon'])
    st.map(df)

    #======================================

    #==========================================



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
