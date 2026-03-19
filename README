# AI Assignment – Pathfinding and UGV Navigation

This project implements search algorithms for pathfinding problems, including real-world road networks and grid-based navigation.

---

## Contents

1. Dijkstra’s Algorithm using real map data  
2. UGV path planning with static obstacles  
3. Approach for dynamic obstacles  

---

## Part 1: Dijkstra’s Algorithm (Real Map)

- Road network is taken from OpenStreetMap using OSMNX  
- User enters latitude and longitude for start and goal  
- Dijkstra’s algorithm (using heapq) is used to find shortest path  

### Features
- Works on real-world road data  
- Computes shortest distance  
- Optional route visualization  

---

## Part 2: UGV Path Planning (Static Obstacles)

- Grid-based environment  
- Obstacles are generated randomly  
- A* algorithm is used for pathfinding  

### Obstacle Levels
- 1 → Low  
- 2 → Medium  
- 3 → High  

### Output
- Path found / not found  
- Path length  
- Nodes explored  
- Path trace (coordinates)  

### Note
At higher obstacle densities, a valid path may not exist. The algorithm correctly handles this case.

---

## Part 3: Dynamic Obstacles

In a dynamic environment, obstacles are not known beforehand and may change during movement. The UGV uses sensors such as cameras or LiDAR to detect obstacles in real time.

Since the initial path may become invalid, the UGV continuously updates its path while moving. When a new obstacle is detected, a new path is computed from the current position to the goal.

This can be done using replanning methods such as Repeated A* or D*, which update the path efficiently.

---

## Installation

Create a virtual environment (recommended):
