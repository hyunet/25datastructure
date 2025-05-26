import streamlit as st
import random
import matplotlib.pyplot as plt


def bubble_sort_trace(arr):
    trace = []
    a = arr[:]
    trace.append(a[:])
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trace.append(a[:])
    return trace


def plot_step(data, step):
    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data, color="skyblue")
    ax.set_title(f"Step {step}")
    st.pyplot(fig)


st.title("🧮 정렬 알고리즘 시각화 (Bubble Sort)")

if st.button("정렬 시작"):
    array = list(range(1, 31))
    random.shuffle(array)
    trace = bubble_sort_trace(array)
    step = st.slider("정렬 단계 선택", 0, len(trace) - 1, 0)
    plot_step(trace[step], step)

st.markdown("""
---
📌 다양한 정렬 알고리즘 (삽입, 선택, 퀵, 머지 등) 시각화도 확장 가능합니다.
""")
