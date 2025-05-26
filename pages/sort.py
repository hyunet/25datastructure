import streamlit as st
import random
import time

# 버블 정렬 실행 시 trace와 swap 위치 저장
def bubble_sort_trace(arr):
    trace = []
    swaps = []
    a = arr[:]
    trace.append((a[:], -1, False))
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            swapped = False
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
            trace.append((a[:], j, swapped))
    return trace

# HTML 스타일 블록 렌더링 함수
def render_block(values, highlight_index=-1, swapped=False):
    box_html = ""
    for i, val in enumerate(values):
        if i == highlight_index or i == highlight_index + 1:
            color = "#ffdd57" if swapped else "#ddd"
        else:
            color = "#f0f0f0"
        box_html += f"<div style='display:inline-block; width:40px; height:40px; margin:4px; text-align:center; line-height:40px; border:1px solid #ccc; background:{color}'>{val}</div>"
    return box_html

# Streamlit UI 시작
st.set_page_config(page_title="버블 정렬 시각화", layout="wide")
st.title("📦 시각적 버블 정렬 단계 보기")

if 'trace' not in st.session_state:
    array = list(range(1, 6))  # 간소화 위해 1~5로 고정
    random.shuffle(array)
    st.session_state.trace = bubble_sort_trace(array)

trace = st.session_state.trace
step = st.slider("정렬 단계", 0, len(trace) - 1, 0)
current, index, swapped = trace[step]

st.markdown("""
<style>
.block-box { display: flex; flex-wrap: wrap; }
</style>
""", unsafe_allow_html=True)

st.markdown("#### 배열 상태")
st.markdown(render_block(current, index, swapped), unsafe_allow_html=True)

if index >= 0:
    st.markdown(f"**비교 중:** {index}번 ↔ {index+1}번 ({'🔁 swap 발생' if swapped else '❌ swap 없음'})")
else:
    st.markdown("**초기 상태**")
