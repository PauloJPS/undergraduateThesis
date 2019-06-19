import igraph as ig
import matplotlib.pyplot as plt
import networkx as nx



def plotInemoChains():
    g = ig.Graph.Watts_Strogatz(1, 12, 1, 0)
    pos = g.layout_circle()
    gnx = ig2nx(g)

    fig, ax = plt.subplots(2, 2)

    ax1 = ax[0]
    ax2 = ax[1]
    
    nx.draw_networkx_nodes(gnx, pos, nodelist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
                            node_shape=r'$\uparrow$', node_size=500, node_color='red', ax=ax1[0])
    nx.draw_networkx_nodes(gnx, pos, nodelist=[0], 
                            node_shape=r'$\downarrow$', node_size=1000, node_color='green', ax=ax1[0])
    #nx.draw_networkx_edges(gnx, pos, ax=ax1[0])

 
    nx.draw_networkx_nodes(gnx, pos, nodelist=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
                            node_shape=r'$\uparrow$', node_size=500, node_color='red', ax=ax1[1])
    nx.draw_networkx_nodes(gnx, pos, nodelist=[0, 2], 
                            node_shape=r'$\downarrow$', node_size=1000, node_color='green', ax=ax1[1])
    #nx.draw_networkx_edges(gnx, pos, ax=ax1[1])


    nx.draw_networkx_nodes(gnx, pos, nodelist=[1, 3, 5, 7, 9, 11], 
                            node_shape=r'$\uparrow$', node_size=500, node_color='red', ax=ax2[0])
    nx.draw_networkx_nodes(gnx, pos, nodelist=[0, 2, 4, 6, 8, 10], 
                            node_shape=r'$\downarrow$', node_size=1000, node_color='green', ax=ax2[0])
    #nx.draw_networkx_edges(gnx, pos, ax=ax2[0])


    nx.draw_networkx_nodes(gnx, pos, nodelist=[11], 
                            node_shape=r'$\uparrow$', node_size=500, node_color='red', ax=ax2[1], label='Spin 1/2')
    nx.draw_networkx_nodes(gnx, pos, nodelist=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                            node_shape=r'$\downarrow$', node_size=1000, node_color='green', ax=ax2[1], label='Spins 1')
    #nx.draw_networkx_edges(gnx, pos, ax=ax2[1])

    ax2[1].legend(loc=1, bbox_to_anchor=(0.2, 2.5), markerscale=0.5, fontsize=12)

    
    ax1[0].set_axis_off()
    ax1[1].set_axis_off()
        
    ax2[0].set_axis_off()
    ax2[1].set_axis_off()
    
    ax1[0].set_xlim((-1.3, 1.3))
    ax1[0].set_ylim((-1.3, 1.3))

    ax1[1].set_xlim((-1.3, 1.3))
    ax1[1].set_ylim((-1.3, 1.3))

    ax2[0].set_xlim((-1.3, 1.3))
    ax2[0].set_ylim((-1.3, 1.3))

    ax2[1].set_xlim((-1.4, 1.4))
    ax2[1].set_ylim((-1.4, 1.4))

    ax1[0].set_title(r'$N_i = 1 $')
    ax1[1].set_title(r'$N_i = 2 $')
        
    ax2[0].set_title(r'$N_i = 6$')
    ax2[1].set_title(r'$N_i = 11 $')

    #plt.tight_layout()
     

def plotNetwor():
    g1 = ig.Graph.Watts_Strogatz(1, 15, 1, 0)
    pos1 = g1.layout_circle()
    gnx1 = ig2nx(g1)
    

    gKS = ig.Graph.Erdos_Renyi(6, 1)
    posKS = gKS.layout_circle()
    gnxKS = ig2nx(gKS)

    
    #fig, ax = plt.subplots(1, 2, figsize=(12, 4.5), aspect='equal')
    fig = plt.figure(figsize=(12, 4.5))
    ax = [plt.subplot(121, aspect='equal'), plt.subplot(122, aspect='equal')]

    nx.draw_networkx_nodes(gnx1, pos1, ax=ax[0], edgecolors='black')
    nx.draw_networkx_nodes(gnxKS, posKS, ax=ax[1], edgecolors='black')

    nx.draw_networkx_edges(gnx1, pos1, ax=ax[0])
    nx.draw_networkx_edges(gnxKS, posKS, ax=ax[1])

    ax[0].set_title('(A)', fontsize=15)
    ax[0].set_axis_off()
    ax[1].set_title('(B)', fontsize=15)
    ax[1].set_axis_off()

    plt.tight_layout()




def ig2nx(g):
    gnx = nx.Graph()
    node_att = [(node.index, node.attributes()) for node in g.vs]
    gnx.add_nodes_from(node_att)
    edge_att = [(edge.source, edge.target, edge.attributes()) for edge in g.es]
    gnx.add_edges_from(edge_att)

    return gnx

