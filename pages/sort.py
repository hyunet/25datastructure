import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 정렬 알고리즘 정의

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

# 시각화 함수

def animate_sort(trace, title="Bubble Sort Animation"):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(trace[0])), trace[0], align="edge", color="skyblue")
    ax.set_title(title)
    ax.set_xlim(0, len(trace[0]))
    ax.set_ylim(0, max(trace[0]) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Step: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        fargs=(bar_rects, iteration),
        frames=trace,
        interval=300,
        repeat=False
    )
    return anim

# Streamlit UI 시작

st.title("🎞️ 정렬 알고리즘 시각화 (Bubble Sort)")
st.markdown("1부터 30까지 숫자 카드를 섞고, 버블 정렬을 통해 정렬 과정을 시각화합니다.")

if st.button("시각화 시작"):
    array = list(range(1, 31))
    random.shuffle(array)
    trace = bubble_sort_trace(array)
    ani = animate_sort(trace)
    st.pyplot(ani._fig)

st.markdown("""
---
📌 더 많은 정렬 알고리즘(삽입, 선택, 퀵, 머지 등)을 시각화로 확장하고 싶으시면 말씀해주세요!
""
