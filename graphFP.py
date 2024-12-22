import networkx as nx
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Create a directed graph
bus_graph = nx.DiGraph()

# Define bus stops and connections (edges with travel times in minutes)
bus_stops = [
    "Downtown", "Midtown", "Corktown", "Greektown", "Eastern Market", "New Center",
    "Southwest", "University District", "Palmer Park", "Belle Isle", "Riverfront",
    "Mexicantown", "Grandmont", "Jefferson", "Hamtramck", "Boston Edison",
    "Brightmoor", "Old Redford", "Indian Village", "East English Village"
]

# Define at least 20 edges with weights (travel times in minutes)
bus_routes = [
    ("Downtown", "Midtown", 10),
    ("Midtown", "Corktown", 15),
    ("Corktown", "Southwest", 10),
    ("Downtown", "Greektown", 5),
    ("Greektown", "Eastern Market", 8),
    ("Eastern Market", "New Center", 20),
    ("New Center", "Midtown", 12),
    ("Southwest", "Downtown", 18),
    ("Midtown", "University District", 14),
    ("University District", "Palmer Park", 10),
    ("Palmer Park", "New Center", 8),
    ("Belle Isle", "Riverfront", 7),
    ("Riverfront", "Mexicantown", 9),
    ("Mexicantown", "Grandmont", 12),
    ("Grandmont", "Jefferson", 15),
    ("Jefferson", "Hamtramck", 10),
    ("Hamtramck", "Boston Edison", 11),
    ("Brightmoor", "Old Redford", 10),
    ("Old Redford", "Indian Village", 18),
    ("Indian Village", "East English Village", 12)
]

# Add stops and routes to the graph
bus_graph.add_weighted_edges_from(bus_routes)

# Map each route to a specific bus
bus_schedules = {
    "Bus 1": ["Downtown", "Midtown", "Corktown", "Southwest"],
    "Bus 2": ["Downtown", "Greektown", "Eastern Market", "New Center"],
    "Bus 3": ["Brightmoor", "Old Redford", "Indian Village", "East English Village"]
}

# Algorithms Implementation
# Dijkstra's Algorithm
print("Dijkstra's Algorithm:")
path_dijkstra = nx.dijkstra_path(bus_graph, source="Downtown", target="New Center")
print(f"Shortest Path (Downtown to New Center): {path_dijkstra}")

# A* Algorithm
print("\nA* Algorithm:")
path_astar = nx.astar_path(bus_graph, source="Downtown", target="New Center")
print(f"Shortest Path (Downtown to New Center): {path_astar}")

# Breadth-First Search
print("\nBreadth-First Search:")
bfs_edges = list(nx.bfs_edges(bus_graph, source="Downtown"))
print(f"Breadth-First Traversal Starting from Downtown: {bfs_edges}")

# Adjacency Matrix
print("\nAdjacency Matrix:")
adjacency_matrix = nx.adjacency_matrix(bus_graph).todense()
print(adjacency_matrix)

# Adjacency List
print("\nAdjacency List:")
adjacency_list = nx.to_dict_of_lists(bus_graph)
for key, value in adjacency_list.items():
    print(f"{key}: {value}")

# Generate Schedules for Multiple Buses
start_time = datetime.strptime("6:00 AM", "%I:%M %p")  # Start time for the first bus
full_schedule = []

for bus, stops in bus_schedules.items():
    for i in range(len(stops) - 1):
        route = (stops[i], stops[i + 1])
        travel_time = dict(bus_graph.edges)[route]["weight"]
        departure_time = start_time + timedelta(minutes=random.randint(0, 120))
        arrival_time = departure_time + timedelta(minutes=travel_time)
        full_schedule.append({
            "Bus": bus,
            "Route": f"{stops[i]} -> {stops[i + 1]}",
            "Departure": departure_time.strftime("%I:%M %p"),
            "Arrival": arrival_time.strftime("%I:%M %p")
        })

# Display the Full Schedule
print("\nBus Schedules:")
for trip in full_schedule:
    print(f"Bus: {trip['Bus']}, Route: {trip['Route']}, Departure: {trip['Departure']}, Arrival: {trip['Arrival']}")

# Visualize the Graph with Bus-Specific Highlights
plt.figure(figsize=(15, 12))
pos = nx.spring_layout(bus_graph, seed=42, k=0.8)  # Further spread nodes for readability
colors = {"Bus 1": "red", "Bus 2": "blue", "Bus 3": "green"}

for bus, stops in bus_schedules.items():
    for i in range(len(stops) - 1):
        nx.draw_networkx_edges(
            bus_graph, pos,
            edgelist=[(stops[i], stops[i + 1])],
            edge_color=colors[bus],
            width=2.0
        )

nx.draw(bus_graph, pos, with_labels=True, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(bus_graph, pos, edge_labels=nx.get_edge_attributes(bus_graph, 'weight'))
plt.title("Detroit Bus Network with Bus Assignments")
plt.show()

# Documentation Notes:
# - Algorithms implemented: Dijkstra's, A*, and Breadth-First Search.
# - Inputs: Graph, source node, and target node for pathfinding algorithms.
# - Outputs: Shortest path or traversal edges.
# - Use cases: Dijkstra's and A* for shortest pathfinding, BFS for traversal or connectivity analysis.
# - Graph represented as adjacency matrix and adjacency list.
