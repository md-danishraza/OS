# process = [AT,BT,pid]

def fcfs(process_list):
    t=0
    gantt = []
    completed = {}

    # sorting the list based of AT
    process_list.sort(key=lambda x: x[0])

    # while processess is running
    while process_list:
        # if process is not arrived yet
        if process_list[0][0] > t:
            t += 1
            gantt.append("idle")
            continue
        else:
            # take and remove from process_list
            process = process_list.pop(0)

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
    processes = [(0, 2, 'P1'), (2, 3, 'P2'), (4, 1, 'P3')]
    fcfs(processes)