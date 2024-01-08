import sys


def convert_alphabet_to_int(char: str):
    """
    알파벳을 숫자로 변환하는 함수이다.
    유니코드 정수를 반환하는 ord 함수를 이용한다.
    리턴은 a = 1, b = 2, ... 와 같이 이뤄진다.
    """
    return int(ord(char)) - int(ord("a")) + 1


def bfs_example():
    from collections import deque

    def bfs(graph, start, visited):
        # 시작 노드 큐에 삽입
        queue = deque([start])

        # 현재 노드 방문 처리
        visited[start] = True

        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 노드 꺼내기
            v = queue.popleft()

            # 필요한 로직 수행
            print("Execute program")

            # 해당 노드의 인접 노드 중에서 방문하지 않은 노드 큐에 삽입하고 방문 처리
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

    visited = [False] * 9

    bfs(graph, 1, visited)


def read_input():
    """
    데이터의 크기가 작은 경우 -> input() 사용.
    데이터의 크기가 큰 경우 -> sys.stdin.readline() 사용.
    """
    x = input()
    y = sys.stdin.readline()


def median(arr):
    """
    중간값 (median) 구하기
    """
    n = len(arr)
    return arr[(n - 1) // 2]


def calculate_n_log_n():
    import math

    func = lambda n: n * math.log2(n)
