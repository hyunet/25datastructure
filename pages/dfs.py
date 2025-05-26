import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

st.title("📌 DFS vs BFS 탐색 비교 실험")
st.write("깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)의 차이를 시각적으로 비교합니다.")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

G = nx.DiGraph()
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(5, 4))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000)
st.pyplot(plt.gcf())

start_node = st.selectbox("시작 노드를 선택하세요", list(graph.keys()), index=0)

if st.button("탐색 실행"):
    start_time = time.time()
    dfs_result = dfs(graph, start_node)
    dfs_time = time.time() - start_time

    start_time = time.time()
    bfs_result = bfs(graph, start_node)
    bfs_time = time.time() - start_time

    st.subheader("🔍 결과 비교")
    st.markdown(f"**DFS 순서:** {dfs_result}  ⏱️ {dfs_time:.6f}초")
    st.markdown(f"**BFS 순서:** {bfs_result}  ⏱️ {bfs_time:.6f}초")
