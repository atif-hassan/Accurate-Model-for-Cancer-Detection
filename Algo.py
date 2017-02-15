import networkx
import matplotlib.pyplot as plt
import numpy
import scipy


def graphGenerator(path):
    
    f = open(path, "r")
    lines = f.readlines()[1:]
    f.close()

    nodes = set()
    G = networkx.Graph()

    for line in lines:
        str1 = line[0:line.index(" ")]
        str2 = line[line.index(" ")+1:line.index(" ", line.index(" ")+1)]
        #weight = line[line.rfind(' ')+1:]

        nodes.add(str1)
        nodes.add(str2)

        #G.add_edge(str1, str2, weight=float(weight))
        G.add_edge(str1, str2)

    for node in nodes:
        G.add_node(node)

    #return G
    networkx.write_graphml(G, "TESTGRAPH.graphml")


def clusterCollectorAndWriter(path, writePath):
    colours = set([])

    refStr = "00000000000"
    strToAdd = "9606.ENSP"

    f = open(path, "r")
    lines = f.readlines()[1:19248]
    f.close()

    f = open(writePath, "w")
    
    for line in lines:
        colours.add(line[line.rfind(' ')+1:].strip().lower())

    colors = list(colours)

    for i in xrange(0, len(colors)):
        #cluster = []
        #print colors[i]
        f.write("Cluster : "+colors[i])
        f.write("\n")
        for j in xrange(0, 19247):
            line = lines[j].strip()
            colour = line[line.rfind(' ')+1:].strip().lower()
            if colors[i] == colour:
                protein = line[line.index('"')+1:line.index('"', line.index('"')+1)]
                NoOfZerosToAdd = len(refStr) - len(protein)
                zeros = ""
                
                for k in xrange(0, NoOfZerosToAdd):
                    zeros+= "0"
                
                newStr = strToAdd + zeros + protein
                f.write(newStr)
                f.write("\n")
        f.write("\n\n")
                
                #cluster.append(newStr)
        #print cluster
        #break


def cancerClusterDetective(path1, path2, path3):
    f1 = open(path1, "r")
    lines1 = f1.readlines()
    f1.close()

    f2 = open(path2, "r")
    lines2 = f2.readlines()
    f2.close()

    f3 = open(path3, "w")

    color = []
    cluster = []

    for line2 in lines2:
        if line2[0]!="9" and len(line2) > 4:
            color.append(line2[10:].strip())

    for c in color:
        cluster.append([c])

    for line1 in lines1:
        clus = ""
        for line2 in lines2:
            if line2[0]!="9" and len(line2) > 4:
                clus = line2[10:].strip()
            if line1.strip() == line2.strip():
                ind = color.index(clus)
                cluster[ind].append(line1.strip())
                break

    for i in xrange(0, len(color)):
        f3.write("Cluster : "+cluster[i][0]+" ("+str(len(cluster[i]))+")"+"\n")
        for j in xrange(1, len(cluster[i])):
            f3.write(cluster[i][j])
            f3.write("\n")
        f3.write("\n\n")
        


    f3.close()
                        
    
    
        

    


datasetPath = "C:\\Users\\atifh\\Desktop\\Summer Internship\\OSLOM2\\9606.protein.links.v10.UW.txt"
clusterPath = "C:\\Users\\atifh\\Desktop\\Summer Internship\\OSLOM2\\9606.protein.links.v10.UW.txt_oslo_files\\pajek_file_0.net"
clusterWritePath = "ClustersUW.txt"
clusterCancerWritePath = "Cancer ClustersUW.txt"
cancerDataSetPath = "Cancer Proteins Mapped to STRING.txt"

#clusterCollectorAndWriter(clusterPath, clusterWritePath)
cancerClusterDetective(cancerDataSetPath, clusterWritePath, clusterCancerWritePath)

#graphGenerator(datasetPath)


#MCL CLUSTERING
'''def testGraph():
    G = networkx.Graph()

    nodes = []
    for i in xrange(1, 5):
        nodes.append(str(i))

    for node in nodes:
        G.add_node(node)

    G.add_edge('1', '2')
    G.add_edge('1', '3')
    G.add_edge('1', '4')

    G.add_edge('2', '1')
    G.add_edge('2', '3')

    G.add_edge('3', '1')
    G.add_edge('3', '2')

    G.add_edge('4', '1')

    nodes = []
    for i in xrange(1, 8):
        nodes.append(str(i))

    for node in nodes:
        G.add_node(node)

    print nodes

    G.add_edge('1', '2')
    G.add_edge('1', '3')
    G.add_edge('1', '4')
    
    G.add_edge('2', '1')
    G.add_edge('2', '3')
    G.add_edge('2', '4')
    G.add_edge('2', '5')
    
    G.add_edge('3', '1')
    G.add_edge('3', '2')
    G.add_edge('3', '4')
    
    G.add_edge('4', '1')
    G.add_edge('4', '3')
    G.add_edge('4', '2')

    G.add_edge('5', '2')
    G.add_edge('5', '6')
    G.add_edge('5', '7')

    G.add_edge('6', '5')
    G.add_edge('6', '7')

    G.add_edge('7', '5')
    G.add_edge('7', '6')

    return G, nodes

    #networkx.write_graphml(G, "TestGraph.graphml")

G, nodes = testGraph()
M = networkx.to_numpy_matrix(G, nodelist = nodes)

numpy.fill_diagonal(M, 1)

#Normalize the matrix
for i in range(len(M)):
    if (numpy.sum(M[i]) > 0):
        M[i] = M[i]/numpy.sum(M[i])

#print M
T = M.transpose()
k=0

while True:
    oldT = T
    T =T * T

    for entry in numpy.nditer(T, op_flags=['readwrite']):
        entry[...] = entry ** 2

    T = T/numpy.sum(T, axis=0)
    if numpy.array_equal(oldT, T):
        break

print T'''
    
