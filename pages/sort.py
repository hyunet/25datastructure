import streamlit as st
import random
import time


def bubble_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left + right)
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


SORTING_ALGOS = {
    "버블 정렬": bubble_sort,
    "선택 정렬": selection_sort,
    "삽입 정렬": insertion_sort,
    "머지 정렬": merge_sort,
    "퀵 정렬": quick_sort
}


def app():
    st.title("🧮 정렬 알고리즘 비교 실험")
    st.markdown("""
    5개의 서로 다른 정렬 알고리즘을 사용해 랜덤 데이터 정렬 속도와 정확성을 비교합니다.
    """)

    arr_size = st.slider("데이터 크기 선택", 10, 200, 50, step=10)
    arr = random.sample(range(1, 1000), arr_size)

    selected = st.multiselect("비교할 정렬 알고리즘 선택", list(SORTING_ALGOS.keys()), default=list(SORTING_ALGOS.keys())[:3])

    if st.button("정렬 실행"):
        st.write("원본 데이터:", arr)
        results = {}

        for algo_name in selected:
            sort_fn = SORTING_ALGOS[algo_name]
            start_time = time.time()
            sorted_arr = sort_fn(arr)
            elapsed = time.time() - start_time
            results[algo_name] = (sorted_arr, elapsed)

        for algo_name, (sorted_arr, elapsed) in results.items():
            st.markdown(f"### 🧪 {algo_name}")
            st.write("정렬 결과:", sorted_arr)
            st.write(f"⏱️ 실행 시간: {elapsed:.6f}초")
