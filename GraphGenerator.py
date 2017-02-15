import csv
from sets import Set
import networkx
import matplotlib.pyplot as plt

f = open("All Proteins Database\\dip20160430.txt", 'r')
lines = csv.reader(f, delimiter='\t')
nodes = Set([])
edges = []

count = 0
uniprot = 0
total = 0

for line in lines:
    #To skip the column header
    if count == 0:
        count+=1
        continue

    str1 = line[9][line[9].index('('):].lower()
    str2 = line[10][line[10].index('('):].lower()

    if "homo sapiens" in str1 or "homo sapiens" in str2:
        #For Interactor A
        try:
            nodes.add(line[0][:line[0].index('|')])
            str1 = line[0][:line[0].index('|')]
        except:
            nodes.add(line[0])
            str1 = line[0]

        #For interactor B
        try:
            nodes.add(line[1][:line[1].index('|')])
            str2 = line[1][:line[1].index('|')]
        except:
            nodes.add(line[1])
            str2 = line[1]

        edges.append([str1, str2])


G = networkx.Graph()


for node in nodes:
    G.add_node(node)


for edge in edges:
    G.add_edge(edge[0], edge[1])

#l = list(nodes)


networkx.write_graphml(G, "Graph.graphml")

#print len(nodes), len(edges)



f.close()
