# priority scheduling (non preemtive)
# since priority is important 
# process_list = [priority,AT,BT,PID]

def priority_non_preemptive(process_list):
    t = 0
    gantt = []
    completed = {}


    while process_list:
        # available = []
        # process that has arrived till now
        available = [p for p in process_list if p[1] <= t]

        if not available:
            # empty list mean no process arrived
            t += 1
            gantt.append("idle")
            # skip the further code lines
            continue
        else:
            # sorting for highest priority
            available.sort(key=lambda x: x[0], reverse=True)
            process = available.pop(0)
            # removing the process from the list
            process_list.remove(process)

            # serving the process
            t += process[2]
            gantt.append(process[3])

            # storing the process in completed list
            ct = t
            tt = ct - process[1]
            wt = tt - process[2]
            completed[process[3]] = [ct, tt, wt]

    print(gantt)
    print(completed)

if __name__ == '__main__':
    process_list = [[1, 0, 5, 1], [2, 2, 4, 2], [3, 3, 3, 3]]
    priority_non_preemptive(process_list)
   