import streamlit as st
from pages import dfs, sort

st.set_page_config(page_title="자료구조 알고리즘 비교 실험", layout="wide")

PAGES = {
    "1. DFS vs BFS 비교": dfs,
    "2. 정렬 알고리즘 비교": sort
}

st.sidebar.title("🔍 알고리즘 비교 실험")
selection = st.sidebar.radio("페이지를 선택하세요", list(PAGES.keys()))

page_function = PAGES[selection]
page_function.app()
