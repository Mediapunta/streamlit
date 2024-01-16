import streamlit as st
from PIL import Image

# Markdown 문법을 st.markdown으로, caption, Latex Code block을 활용가능
## Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
            "   - item 1.1\n"
            "   - item 1.2\n"
            "- item 2\n"
            "- item 3")
st.markdown("1. item 1\n"
            "   1. item 1.1\n"
            "   2. item 1.2\n"
            "2. item 2\n"
            "3. item 3")



# 하얀색 배경 필요시 
#st.write('이거슨 Streamlit이여')

st.sidebar.title('사이드바')
st.title('이거슨 Streamlit이여')
st.header('이거슨 Streamlit Header여')
st.subheader('이거슨 Streamlit subHeader여')

## MultiSelect
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
                          ("운동", "IT기기", "브이로그",
                           "먹방", "반려동물", "맛집 리뷰"))
st.write(len(location), "가지를 선택했습니다.")

## Select Box
occupation = st.selectbox("직군을 선택하세요.",
 ["Backend Developer",
 "Frontend Developer",
 "ML Engineer",
 "Data Engineer",
 "Database Administrator",
 "Data Scientist",
 "Data Analyst",
 "Security Engineer"])
st.write("당신의 직군은 ", occupation, " 입니다.")

## Buttons
if st.button("누르면 죽을수도 있어"):
 st.text("-ㅠ-")

number = st.slider("Pick a number", 0, 100)

file = st.file_uploader("Pick a file")

color = st.color_picker("Pick a color")

pet = st.radio("Pick a pet", [":rainbow[Dog]", "***Cat***", "Bird :movie_camera:"])

date = st.date_input("Pick a date")
st.altair_chart(my_chart)

df = pd.read_csv("my_data.csv")
st.line_chart(df)

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
aws_img = Image.open("aws_white.png")
LambdaRamsey_img = Image.open("Lambda_SAM.png")

aws_img()
LambdaRamsey_img()




import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
#import streamlit as st

iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
print(df)

st.subheader('입력혀')
st.table(df.head())

st.subheader('data frame 이여')
st.dataframe(df.head())

# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title('Iris Species🌸')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
)
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df[df['species']== select_species]
# 선택한 종의 맨 처음 5행을 보여줍니다 
st.table(tmp_df.head())       
