from math import inf

def dijkstra(adj, weights, a):
	d = [i for i in range(0, len(adj))];
	for i in d:
		d[i] = inf;
	d[a] = 0;
	V = [False] * len(d);
	p = [None] * len(d);
	p[a] = [0];
	while False in V:
		min_d = inf;
		v = None;
		for i in range(0, len(d)):
			if V[i] == False and d[i] <= min_d:
				v = i;
				min_d = d[i];
		V[v] = True;
		for j in range (0, len(d)):
			if adj[v][j] == 0:
				continue;
			if d[j] > d[v] + weights[v][j]:
				d[j] = d[v] + weights[v][j]
				p[j] = p[v] + [j];
	return (d, p)
"""
adj = [[0, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 0, 0],
		[1, 1, 0, 1, 0, 1],
		[0, 1, 1, 0, 1, 0],
		[0, 0, 0, 1, 0, 1],
		[1, 0, 1, 0, 1, 0]];

weights = [[0, 7, 9, 0, 0, 14],
		[7, 0, 10, 15, 0, 0],
		[9, 10, 0, 11, 0, 2],
		[0, 15, 11, 0, 6, 0],
		[0, 0, 0, 6, 0, 6],
		[14, 0, 2, 0, 9, 0]];
"""
adj = [[0, 1, 1, 1, 0],
	[1, 0, 1, 0, 1],
	[1, 1, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[0, 1, 0, 1, 0]];
weights = [[0, 3, 1, 5, 0],
	[3, 0, 1, 0, 2],
	[1, 1, 0, 0, 0],
	[5, 0, 0, 0, 6],
	[0, 2, 0, 6, 0]];

print(dijkstra(adj, weights, 0));
