# shortest job first non preemptive
# since AT is significant for this also we are placing it first
# process = [AT,BT,pid]

def sjfnp(process_list):
    t = 0
    gantt = []
    completed = {}

    # while processes is present
    while process_list:
        # available = []
        # process that has arrived till now
        available = [p for p in process_list if p[0] <= t]

        if not available:
            # empty list mean no process arrived
            t += 1
            gantt.append("idle")
            continue
        else:
            # find process with minimum BT
            available.sort()
            process = available.pop(0)
            process_list.remove(process)

            gantt.append(process[2])
            # times taken to execute BT
            t += process[1]

            pid = process[2]
            # completion time
            ct = t
            # turnaround time = completion time - arrival time
            tt = ct - process[0]
            # waiting time = tt - bt
            wt = tt - process[1]

            # adding to completed
            completed[pid] = [ct,tt,wt]

    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[0, 5, 1], [2, 4, 2], [3, 3, 3]]
    sjfnp(process_list)
    
    

