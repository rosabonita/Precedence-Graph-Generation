import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#Getting the lengths of the files    
tvg_len = file_len('tvg.txt')
pred1_len = file_len('pred1.txt')
pred2_len = file_len('pred2.txt')
pred3_len = file_len('pred3.txt')
pred4_len = file_len('pred4.txt')
pred5_len = file_len('pred5.txt')
pred6_len = file_len('pred6.txt')
pred7_len = file_len('pred7.txt')

#Opening the files
tvg_file = open('tvg.txt', 'r')
pred1_file = open('pred1.txt', 'r')
pred2_file = open('pred2.txt', 'r')
pred3_file = open('pred3.txt', 'r')
pred4_file = open('pred4.txt', 'r')
pred5_file = open('pred5.txt', 'r')
pred6_file = open('pred6.txt', 'r')
pred7_file = open('pred7.txt', 'r')

#Reading the lines of the files
tvg_lines_file = tvg_file.readlines()
pred1_lines_file = pred1_file.readlines()
pred2_lines_file = pred2_file.readlines()
pred3_lines_file = pred3_file.readlines()
pred4_lines_file = pred4_file.readlines()
pred5_lines_file = pred5_file.readlines()
pred6_lines_file = pred6_file.readlines()
pred7_lines_file = pred7_file.readlines()

#Saving the lines to lists of strings
tvg_lines_list =[]
pred1_lines_list = []
pred2_lines_list = []
pred3_lines_list = []
pred4_lines_list = []
pred5_lines_list = []
pred6_lines_list = []
pred7_lines_list = []

count = 0

while count < tvg_len:
    tvg_lines_file[count] = tvg_lines_list.append(tvg_lines_file[count])
    pred1_lines_file[count] = pred1_lines_list.append(pred1_lines_file[count])
    pred2_lines_file[count] = pred2_lines_list.append(pred2_lines_file[count])
    pred3_lines_file[count] = pred3_lines_list.append(pred3_lines_file[count])
    pred4_lines_file[count] = pred4_lines_list.append(pred4_lines_file[count])
    pred5_lines_file[count] = pred5_lines_list.append(pred5_lines_file[count])
    pred6_lines_file[count] = pred6_lines_list.append(pred6_lines_file[count])
    pred7_lines_file[count] = pred7_lines_list.append(pred7_lines_file[count])
    count += 1

#Creating the nodes 1st Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred1_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred1_lines_list[count])
        count += 1

#Creating the 2nd Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        if pred2_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred2_lines_list[count])
        count += 1

#Creating the 3rd Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred3_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred3_lines_list[count])
        count += 1

#Creating the 4th Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred4_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred4_lines_list[count])
        count += 1
        
#Creating the 5th Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred5_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred5_lines_list[count])
        count += 1

#Creating the 6th Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred6_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred6_lines_list[count])
        count += 1

#Creating the 7th Precedence edges
count  = 0

while count < tvg_len:
    if tvg_lines_list[count].startswith('empty'):
        count += 1
    else:
        G.add_node(tvg_lines_list[count])
        if pred7_lines_list[count].startswith('empty'):
            count += 1
        else:
            G.add_edge(tvg_lines_list[count],pred7_lines_list[count])
        count += 1
        
#Reversing the arrow direction            
def backwards(self): 
    H=self.__class__()  
    H.add_nodes_from(self) 
    H.add_edges_from([(v,u) for (u,v) in self.edges_iter()]) 
    return H   
    
H = backwards(G)

#Removing the labels from the the nodes in the NX graph
nx.draw(H, node_size=80, with_labels=False)
plt.savefig("pred1.png")

#Writing the DOT file for use with Graph Viz
nx.drawing.write_dot(H,'pred1.dot')
