import heapq

def create_graph(inp):
    lines = inp.readlines()
    graph = {}

    for line in lines:
        temp = line.split()
        node = temp[0] 
        heuristic = int(temp[1])  
        
        graph[node] = {'heuristic': heuristic, 'children': []}

        for i in range(2, len(temp), 2):
            child = temp[i]
            cost = int(temp[i + 1])  
            graph[node]['children'].append((child, cost))


    #print(graph)
    return graph


def a_star(graph, start, goal):
    
    priorityQ = [(graph[start]['heuristic'], start)]
    heapq.heapify(priorityQ)

    cost_dict={}
    for node in graph:
        if node==start:
            cost_dict[node] = 0
        else:
            cost_dict[node]=float('inf') 

    parent = {start: None}
    visited_list = []

    while priorityQ:
        current_f_n, current_node = heapq.heappop(priorityQ)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path, cost_dict[path[0]]
        

        visited_list.append(current_node)
        children_list=graph[current_node]['children']

        for child, cost in children_list:
            if child not in visited_list:
                temp_cost = cost_dict[current_node] + cost
                if temp_cost < cost_dict[child]:
                    cost_dict[child] = temp_cost
                    f_n= temp_cost + graph[child]['heuristic']
                    heapq.heappush(priorityQ, (f_n, child))
                    parent[child] = current_node

    return None,None


if __name__ == "__main__":
    
    inp = open("input.txt", "r")
    graph = create_graph(inp)

    source = input("Start node: ")
    goal = input("Destination: ")

    path, cost = a_star(graph, source, goal)

    if path is not None:
        print("Path: ", " -> ".join(path[::-1]))
        print(f"Total distance: {cost} km")
    else:
        print("NO PATH FOUND")