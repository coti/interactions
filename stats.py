import networkx as nx

g = nx.Graph(nx.drawing.nx_agraph.read_dot("graphe.dot"))

print("diameter:", nx.diameter(g))
print("radius:", nx.radius(g))
print("eccentricities:")
for node, ecc in sorted(nx.eccentricity(g).items()) :
    print(" -", node, "=", ecc)
