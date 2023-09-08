def eulerian(G):
    n = len(G)
    out_deg = [0] * n
    in_deg  = [0] * n

    for u in range(n):
        for v in G[u]:
            out_deg[u] += 1
            in_deg[v]  += 1

    path_begin = path_end = -1
    for i in range(n):
        if out_deg[i] == in_deg[i]: continue
        if out_deg[i] - in_deg[i] == 1:
            if path_begin >= 0: break
            path_begin = i
            continue
        if in_deg[i] - out_deg[i] == 1:
            if path_end >= 0: break
            path_end = i
            continue
        break
    # If not broken, there might be a path or a cycle
    else:
        # Only begin or only end
        if path_end * path_begin < 0:
            return None, []
        # Cycle
        elif path_begin == path_end == -1:
            return None, out_deg  # In a cycle we can start no matter where, hence return None
        # Path
        else:
            return path_begin, out_deg
    # Otherwise, nothing
    return -1, []


def euler(G):
    """
    Return a cycle if there is a cycle or a path if only a path exists.
    If there is neither cycle nor path return an empty result.
    """
    begin, out = eulerian(G)

    # If no cycle nor path
    if not out: return []

    # If there is a cycle, choose the first vertex which has neighbours
    # as the beginning vertex
    if begin is None:
        for i in range(len(G)):
            if G[i]:
                begin = i
                break

    result = []

    def dfs(u):
        while out[u]:
            out[u] -= 1
            v = G[u][out[u]]
            dfs(v)
        result.append(u)

    dfs(begin)

    return result[::-1]