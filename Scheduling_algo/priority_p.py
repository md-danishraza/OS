# # priority preempive
# # since priority is important so placed at fist
# # process_list = [priority,bt,at,pid]

# def priority_preemptive(process_list):
#     t = 0
#     gantt = []
#     completed = {}
#     # storing pid and bt for calculating wt
#     burst_time = {}
#     for process in process_list:
#         burst_time[process[3]] = process[1]

    
#     while process_list:
#         # checing arrival 
#         arrived = [p for p in process_list if p[2] <= t]

#         if not arrived:
#             t += 1
#             gantt.append("idle")
#         else:
#             # sorting by priority
#             arrived.sort()

#             # taking the highest priority process
#             process = arrived.pop()
#             process_list.remove(process)

#             t += 1
#             # decreasing the bt of process
#             process[1] -= 1
#             gantt.append(process[3])

#             if process[1] == 0:
#                 ct = t
#                 pid = process[3]
#                 tt = ct - process[2]
#                 wt = tt - burst_time[pid]

#                 completed[pid] = [ct,tt,wt]
                
#             else:
#                 # process is not completed so putting it back in the list
#                 process_list.append(process)

#     print(gantt)
#     print(completed)


# if __name__ == '__main__':

#     process_list = [[3, 0, 1, 'P1'], [2, 2, 2, 'P2'], [1, 4, 3, 'P3']]
#     priority_preemptive(process_list)

# priority preemptive
# since priority is important, it is placed first
# process_list = [priority,bt,at,pid]

def priority_preemptive(process_list):
    t = 0
    gantt = []
    completed = {}
    # storing pid and burst time for calculating wait time later
    burst_time = {}
    for process in process_list:
        burst_time[process[3]] = process[1]

    while process_list:
        # checking processes that have arrived
        arrived = [p for p in process_list if p[2] <= t]

        if not arrived:
            t += 1
            gantt.append("idle")
        else:
            # sorting by priority in descending order (larger number = higher priority)
            arrived.sort(key=lambda x: x[0], reverse=True)

            # taking the highest priority process (which will be the first after sorting)
            process = arrived[0]
            process_list.remove(process)

            t += 1
            # decreasing the burst time of the process
            process[1] -= 1
            gantt.append(process[3])

            if process[1] == 0:
                # process is completed
                ct = t  # completion time
                pid = process[3]  # process id
                tt = ct - process[2]  # turnaround time
                wt = tt - burst_time[pid]  # waiting time

                completed[pid] = [ct, tt, wt]
            else:
                # process is not completed, so put it back in the list
                process_list.append(process)

    print("Gantt Chart:", gantt)
    print("Completed Process Info:", completed)


if __name__ == '__main__':
    # priority, burst time, arrival time, process id
    process_list = [[3, 5, 0, 'P1'], [2, 3, 1, 'P2'], [1, 4, 2, 'P3']]
    priority_preemptive(process_list)
