import igraph as ig
import matplotlib.pyplot as plt
import networkx as nx


def plotNetwor():
    g1 = ig.Graph.Watts_Strogatz(1, 15, 1, 0)
    pos1 = g1.layout_circle()
    gnx1 = ig2nx(g1)
    

    gKS = ig.Graph.Erdos_Renyi(6, 1)
    posKS = gKS.layout_circle()
    gnxKS = ig2nx(gKS)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    
    nx.draw_networkx_nodes(gnx1, pos1, ax=ax[0])
    nx.draw_networkx_nodes(gnxKS, posKS, ax=ax[1])

    nx.draw_networkx_edges(gnx1, pos1, ax=ax[0])
    nx.draw_networkx_edges(gnxKS, posKS, ax=ax[1])

    ax[0].set_title('(A) Heisenberg 1-D', fontsize=15)
    ax[0].set_axis_off()
    ax[1].set_title('(B) Heisenberg TTI', fontsize=15)
    ax[1].set_axis_off()

    plt.tight_layout()




def ig2nx(g):
    gnx = nx.Graph()
    node_att = [(node.index, node.attributes()) for node in g.vs]
    gnx.add_nodes_from(node_att)
    edge_att = [(edge.source, edge.target, edge.attributes()) for edge in g.es]
    gnx.add_edges_from(edge_att)

    return gnx

