class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def calculate_times(processes):
    n = len(processes)
    total_waiting_time = 0
    total_turnaround_time = 0
    
    # Start with the first process
    current_time = processes[0].arrival_time
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
    
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# List of processes with (pid, arrival_time, burst_time)
processes = [
    Process(1, 0, 4),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 2),
    Process(5, 4, 5)
]

# Sort processes by arrival time
processes.sort(key=lambda x: x.arrival_time)

avg_waiting_time, avg_turnaround_time = calculate_times(processes)

print(f"Average Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Output the waiting time and turnaround time for each process
for process in processes:
    print(f"Process {process.pid}: Waiting Time = {process.waiting_time}, Turnaround Time = {process.turnaround_time}")
