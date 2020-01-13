
MEME SPREADING MODEL
Consider the following meme spreading model.
• A meme initiates at node in the social network at timestep=0;
• At each timestep t > 0, each node with this meme spreads the meme to all its neighbours.

Implement this algorithm with Python. Load the network in graph.dat, and determine which node should you choose as the starting node of a meme, in orderto get the maximum number of nodes with the meme at t=2.






HERDING SCRIPTS
Consider the following (rather simple) generative model for the Web, where a webpagecan be seen as a node, and a hyperlink between two webpages can be seen as a link.

• It starts with a single node at timestep t = 1. The node has one link to itself,meaning it has degree k=2(one indegree and one outdegree);
•At each timestep t>1, a new node (without a self-loop) joins the Web, and createsa link to one of the existing nodes.

1) Write a program to simulate this generative model for both situations, and plot the degree distribution at t=10000. What axis scales do you use for each situation? Why?

2) Write your own function to calculate the entropy of a (discrete) probability distribution(with base 2), and apply it to both degree distributions in the previous task