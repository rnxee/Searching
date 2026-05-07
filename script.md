0:30-1:35 - Code Walkthrough
and now i'll walkthrough you to the highlights of our code, i'll open first evacuation_system.py. The program uses only Python standard libraries such as argparse, csv,
heapq, math, and dataclasses library
First is, the program reads and loads the dataset, it reads the victims, nodes and graph dataset using their own read functions, each read function has their own required
columns and also checks if edge weights are non-negative values.
Next is to cluster the victims into their nearest cluster, we used K-Means algorithm to cluster them and it is implemented manually.
First, it chooses deterministic starting centroids using the choose initial centroids function.
def choose_initial_centroids(points, k):
 ordered_points = sorted(points)
 for index in range(k):
 spread_index = round(index * (len(ordered_points) - 1) / (k - 1))
 centroids.append(ordered_points[spread_index])
then for each iteration each victim point is assigned to the nearest centroid using Euclidean distance. After that, each centroid is recomputed as the mean of the points
assigned to it. The loop repeats until the centroids stop moving or the maximum iteration limit is reached.
Now after clustering, the next thing is to find the best routes for each victims cluster, plan_routes this function uses the A* algorithm. A* uses a priority queue from
heapq, using a best_cost table, and a came_from map to reconstruct the best route. The route cost is risk-aware as it computes them using this formula (point to edge_cost
Function):
distance * (1.0 + risk_weight * flood_risk)
This means roads with higher flood risk become more expensive, so the algorithm can prefer safer routes even if a route is not simply the shortest by distance.
we used A* because the report found it more suitable than Dijkstra's for real time evacuation because A* avoid unecessary exploration by using heuristic to guide the
search toward the destination
1:35-2:50 - Live Demonstration
Now I will run the program using the sample dataset.
First, I will verify that the dataset loads correctly.
python3 evacuation_system.py --stage load
The output shows 12 victim or GPS points, 12 road and shelter nodes, 3 available shelters, and 15 road edges. This confirms that the program successfully loaded and
validated the sample data.
Next, I will run the K-Means processing stage.
python3 evacuation_system.py --stage cluster
The output shows that K-Means converged in 2 iterations. It grouped the 12 victim points into 3 clusters. Each cluster has 4 victims, and the program prints the final
centroid and the victim IDs assigned to each cluster.
Finally, I will run the full routing output.
python3 evacuation_system.py --stage route
The output now includes the A* routing result for each cluster. For example, Cluster 1 starts at node N2 and is routed to shelter S1. The program prints the route path, total
cost, and remaining shelter capacity. Cluster 2 is routed from N8 to S2, and Cluster 3 is routed from N5 to S1.
This demonstrates the complete hybrid process: first grouping people with K-Means, then routing those groups with A*.
