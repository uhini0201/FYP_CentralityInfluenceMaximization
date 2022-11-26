import snap
import re

f = open("Graphdata/retweet.txt")
s = f.read()
s1 = re.split('\n', s)
G1 = snap.PUNGraph.New()

a = re.split(' ', s1[0])

for i in range(0, int(a[0])):
	G1.AddNode(i)

for i in range(1, int(a[1]) + 1):
	b = re.split(' ', s1[i])
	G1.AddEdge(int(b[0]), int(b[1]))

EccCentr = dict()

for NI in G1.Nodes():
	EccCentr[NI.GetId()] = snap.GetNodeEcc(G1, NI.GetId(), True)
	print("node: %d centrality: %f" % (NI.GetId(), EccCentr[NI.GetId()]))

EdgePara = dict()

for i in range(1, int(a[1]) +1):
	c = re.split(' ', s1[i])
	if EccCentr[int(c[0])] == 0 and EccCentr[int(c[1])] == 0:
		EdgePara[(int(c[0]), int(c[1]))] = 0
		EdgePara[(int(c[1]), int(c[0]))] = 0
	else:
		EdgePara[(int(c[0]), int(c[1]))] = float(1 * EccCentr[int(c[0])]) / (EccCentr[int(c[0])] + EccCentr[int(c[1])])
		EdgePara[(int(c[1]), int(c[0]))] = float(1 * EccCentr[int(c[1])]) / (EccCentr[int(c[0])] + EccCentr[int(c[1])])

print(EdgePara)