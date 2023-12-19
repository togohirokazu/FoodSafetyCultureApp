import streamlit as st
import pandas as pd
import plotly.express as px

answer = ["そう思わない", 
          "あまりそう思わない", 
          "どちらとも言えない", 
          "ややそう思う", 
          "そう思う"]

#ここからアプリ開始
st.title('食品安全文化の計測アプリ')

st.write('この施設における食品安全対策について、意見を聞かせてください。')
st.write('この施設で経験したことのうち、もっとも当てはまる欄にチェックしてください。匿名のため、名前は記入しないでください。')

st.write('**この飲食店では...**')

# 従業員のコミットメント
q1 = st.radio("１．誰も見ていない時でも、従業員は食品安全のルールを守っている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q2 = st.radio("２．従業員同士が食品安全のルールを守るよう励まし合っている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q3 = st.radio("３．従業員はそれぞれの役割における食品安全に責任を持っている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q4 = st.radio("４．従業員はルールに従い手を洗っている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)

# 資源
q5 = st.radio("５．素手で食品に触れないように、手袋や器具が十分に用意されている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q6 = st.radio("６．近くに手洗いシンクがあり、手洗いを行いやすい。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q7 = st.radio("７．手洗いシンクは、お湯が出て、石鹸、ペーパータオルなどがある。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)

# 責任者のコミットメント
q8 = st.radio("８．忙しい時、責任者は食品安全のルールを守ることよりも、料理を出すことを優先する。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q9 = st.radio("９．仕事が多すぎるため、従業員は手を抜かざるを得ない。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q10 = st.radio("１０．従業員が食品安全のルールを守っていない時、責任者は見て見ぬふりをする。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)

# リーダーシップ
q11 = st.radio("１１． 私が仕事をする上で十分な食品安全に関するトレーニングを提供してくれる。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q12 = st.radio("１２．責任者は従業員からフィードバックを得て、食品安全を改善している。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q13 = st.radio("１３．食品安全は、掲示物、ポスター、シフトミーティングなどで強調されている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q14 = st.radio("１４．従業員が食品安全のルールを守ることが積極的に評価されている。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q15 = st.radio("１５．責任者は私の役割、責任を説明してくれる。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)
q16 = st.radio("１６．従業員は、この施設で従業員に求められる食品安全のレベルを理解している。", 
              [1,2,3,4,5], 
              captions = answer, index=2, horizontal=True)

m1 = round((q1 + q2 + q3 + q4) / 4 ,2)
m2 = round((q5 + q6 + q7) / 3, 2)
m3 = round((q8 + q9 + q10) / 3, 2)
m4 = round((q11 + q12 + q13 + q14 + q15 + q16) / 6, 2)


#submit = st.button('提出')

if st.button('提出'):
    df = pd.DataFrame(dict(
        r=[m1, m2, m3, m4],
        theta=['従業員のコミットメント','資源','責任者のコミットメント', 'リーダーシップ']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig)
    st.write('従業員のコミットメント：', m1)
    st.write('資源：', m2)
    st.write('責任者のコミットメント：', m3)
    st.write('リーダーシップ：', m4)