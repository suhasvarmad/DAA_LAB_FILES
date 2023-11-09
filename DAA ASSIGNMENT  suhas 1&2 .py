
# First code 


class Teacher:
    def __init__(self, arrival_day, lectures_needed, curse_level):
        self.arrival_day = arrival_day
        self.lectures_needed = lectures_needed
        self.curse_level = curse_level

def schedule_lectures(N, D, teachers):
    teachers.sort(key=lambda teacher: teacher.arrival_day)
    total_curse = 0
    current_day = 1

    for teacher in teachers:
        if current_day > D:
            break

        lectures_to_schedule = min(D - current_day + 1, teacher.lectures_needed)
        total_curse += teacher.curse_level * (teacher.lectures_needed - lectures_to_schedule)
        current_day += lectures_to_schedule

    return total_curse

# Reading input
N, D = map(int, input().split())
teachers = []

for _ in range(N):
    Di, Ti, Si = map(int, input().split())
    teachers.append(Teacher(Di, Ti, Si))

# Calling the function and printing the result
min_curse = schedule_lectures(N, D, teachers)
print(min_curse)

#input 
# 3 4
# 1 2 300
# 2 2 100

#output
# 100




# Secound code


import heapq

def calculate_shortest_time_to_vaccine(num_universes, num_portals, portals, demon_times):
    # Create an adjacency list to represent the multiverse with portals
    graph = [[] for _ in range(num_universes)]
    for start, end, time in portals:
        graph[start - 1].append((end - 1, time))
        graph[end - 1].append((start - 1, time))
    
    # Initialize a list to track the shortest time to reach each universe
    shortest_time = [float('inf')] * num_universes
    shortest_time[0] = 0
    
    # Initialize a priority queue for Dijkstra's algorithm
    priority_queue = [(0, 0)]  # (time, universe)
    
    while priority_queue:
        current_time, current_universe = heapq.heappop(priority_queue)
        
        # Check if we have reached the nth universe
        if current_universe == num_universes - 1:
            return current_time
        
        # Check for the next possible universes to visit
        for neighbor, travel_time in graph[current_universe]:
            # Calculate the waiting time due to demons
            waiting_time = 0
            for demon_time in demon_times[neighbor]:
                if demon_time >= current_time + waiting_time:
                    break
                waiting_time += 1
            
            # Calculate the total time to reach the neighbor universe
            total_time = current_time + waiting_time + travel_time
            
            # Update the shortest time if it's shorter
            if total_time < shortest_time[neighbor]:
                shortest_time[neighbor] = total_time
                heapq.heappush(priority_queue, (total_time, neighbor))
    
    # If we can't reach the nth universe, return -1
    return -1

# Read input
num_universes, num_portals = map(int, input().split())
portals = [list(map(int, input().split())) for _ in range(num_portals)]
demon_times = [list(map(int, input().split()))[1:] for _ in range(num_universes)]

# Calculate and print the shortest time
result = calculate_shortest_time_to_vaccine(num_universes, num_portals, portals, demon_times)
print(result)

# INPUT
# 4 4 
# 1 2 3
# 1 3 2 
# 2 4 2
# 3 4 3 
# 0
# 1 4 
# 2 2 3
# 0

# OUTPUT
# 5

