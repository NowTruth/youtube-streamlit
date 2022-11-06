from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')  #タイトルの追加

st.write('DataFrame')   #テキストの追加

#表データの追加
df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#表データの表示
#st.write(df)でも表示できるが、widthやheightを指定する引数が用意されていない
#st.dataframe(df, width=300, height=180)
st.dataframe(df.style.highlight_max(axis=0), width=300, height=180)  #axis=0のとき列、1のとき行をhighlight表示する

st.table(df)  #staticなテーブルを用意したいときに用いる、ソートとかもできない

"""
# 章
## 節
### 項
```Python  #pythonのコードを書きますよという宣言
import streamlit as st
import numpy as np
import pandas as pd;
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
) 

st.line_chart(df2) #折れ線グラフ表示
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']  #新宿付近の100箇所の緯度と経度のデータを用意
)

st.map(df3)

st.write('Display Image')
img = Image.open('IMG_3734.jpeg')
st.image(img, caption='Ryo Imai', use_column_width=True)