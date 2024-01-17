import networkx as nx
import matplotlib.pyplot as plt

nxG = nx.Graph()


"""
nxG.add_node(2)

nxG.add_edge(1,2)
nxG.add_edge(1,3)
nxG.add_edge(2,3)

"""


NxNodeList = ['alice','bob','claire','diane','eve','fred','gary','helen','ines','james','karen','lauren']
nxG.add_nodes_from(NxNodeList)

alice = ['bob','eve','helen']
bob=['alice','fred','james']
claire=['diane','eve','karen']
diane= ['claire','gary','helen']
eve=['alice','ines','james']
fred=['bob','james','ines']
gary=['diane','james','bob']
helen=['alice','fred','claire']
ines=['eve','helen','fred']
james=['bob','eve','ines']
karen=['alice','lauren','helen']
lauren=['claire','ines','alice']

#for i in range (0,(len(alice)-1)):
 #   nxG.add_edge('alice',alice[i])

for k in NxNodeList:
    for i in range (0,(len(alice)-1)):
        nxG.add_edge(k,k[i])


nx.draw(nxG)
plt.savefig("filename.png")
plt.show()