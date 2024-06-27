
def is_safe(allocation, max, available, num_processes, num_resources):
    need = [[0] * num_resources for _ in range(num_processes)]
    
    # Calculate the need matrix
    for i in range(num_processes):
        for j in range(num_resources):
            need[i][j] = max[i][j] - allocation[i][j]
    
    # Initialize the finished array and the work vector
    finished = [False] * num_processes
    work = available[:]
    
    # Start checking for safe sequence
    while True:
        found = False
        for p in range(num_processes):
            if not finished[p]:
                if all(need[p][j] <= work[j] for j in range(num_resources)):
                    for j in range(num_resources):
                        work[j] += allocation[p][j]
                    finished[p] = True
                    found = True
        if not found:
            break

    return all(finished)

# Example usage
num_processes = 5
num_resources = 3

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

max = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

available = [3, 3, 2]

if is_safe(allocation, max, available, num_processes, num_resources):
    print("System is in a safe state.")
else:
    print("System is not in a safe state.")
