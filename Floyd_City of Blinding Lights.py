import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3
        dist[u][v] = w  # last edge between a pair overrides earlier ones

    # Floyd-Warshall
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    q = int(data[idx])
    idx += 1
    out = []
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        d = dist[a][b]
        out.append(str(-1 if d == INF else d))

    print("\n".join(out))

main()