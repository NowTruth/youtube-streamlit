#インターラクティブなウィジェット
#インターラクティブ：双方向、対話、動的な変化を及ぼしてくる
#ウィジェット：UIのこと

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

st.write('プレグレスバーの表示')
'Start!!'

#空の要素をlates_iterationに代入する
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

#チェックボックスを用いて表示の可否を実現する
if st.checkbox('Show Image'):
    img = Image.open('IMG_3734.jpeg')
    st.image(img, caption='Ryo Imai', use_column_width=True)

#セレクトボックス
#optionという変数にセレクトボックスで選択した動的な値を入れて表示する。
option = st.selectbox(
          'あなたが好きな数字を教えてください',
          list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

#カラムでレイアウト表示したい時にはcolumnを定義してあげる
left_column, right_column = st.columns(2)

#左カラムのボタンが押されたら右側にテキストを表示する
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答を書く')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答を書く')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の回答を書く')

#テキストボックス
#textという変数にテキストボックスに入力した動的な値を入れて表示する。
#sidebarを付け加えることでサイドバーに表示することができる
#text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味：', text

#スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition



