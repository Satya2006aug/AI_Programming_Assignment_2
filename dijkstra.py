import osmnx as ox
import heapq

# Load a smaller area (full India is too slow)
place = "Delhi, India"
G = ox.graph_from_place(place, network_type='drive')
G = G.to_undirected()

# Dijkstra using priority queue
def dijkstra(graph, start, end):
    pq = [(0, start)]

    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    parent = {node: None for node in graph.nodes}

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_node == end:
            break

        for neighbor in graph.neighbors(curr_node):
            edge_data = graph.get_edge_data(curr_node, neighbor)

            # get road length
            if isinstance(edge_data, dict):
                edge = list(edge_data.values())[0]
                weight = edge.get('length', 1)
            else:
                weight = edge_data.get('length', 1)

            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = curr_node
                heapq.heappush(pq, (new_dist, neighbor))

    # build path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, distances[end]

# take input from user
print("Enter START location:")
start_lat = float(input("Latitude: "))
start_lon = float(input("Longitude: "))

print("\nEnter GOAL location:")
end_lat = float(input("Latitude: "))
end_lon = float(input("Longitude: "))

# convert coordinates to nearest nodes
start_node = ox.distance.nearest_nodes(G, start_lon, start_lat)
end_node = ox.distance.nearest_nodes(G, end_lon, end_lat)

# run algorithm
path, distance = dijkstra(G, start_node, end_node)

# print result
print("\n--- RESULT ---")
print("Shortest Distance (meters):", round(distance, 2))
print("Number of nodes in path:", len(path))

# show route on map
ox.plot_graph_route(G, path)
