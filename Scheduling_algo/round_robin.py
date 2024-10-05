# preemptive FCFS
#  time quantum 
# process = [AT,BT,pid]


def roundRobin(process_list,time_quantum):
    t = 0
    gantt = []
    completed = {}
    # storing pid and burst time for calculating wait time later
    burst_time = {}
    for i in process_list:
        burst_time[i[2]] = i[1]

    # sorting the process list by AT 
    # so that processess can be sequenced in end
    process_list.sort()


    while process_list:
        # process that has arrived till now
        # in this ordered will be maintained 
        # we are just checking of AT
        available = [p for p in process_list if p[0] <= t]

        if not available:
            # empty list mean no process arrived
            t += 1
            gantt.append("idle")
            continue
        else:
            process = available.pop(0)
            process_list.remove(process)
            # if BT is < time quantum
            # means that process will gets completed
            if process[1]<time_quantum :
                gantt.append(process[2])
                t += process[1]

                pid = process[2]
                tt = t - process[0]
                wt = tt - burst_time[pid]
                completed[process[2]] = [t,tt,wt]

            else:
                # process isn't completed
                t += time_quantum
                gantt.append(process[2])
                process[1] -= time_quantum
                # add this process to the end of the list
                process_list.append(process)

    print(gantt)
    print(completed)



if __name__ == '__main__':
    process_list = [[1, 5, 'P1'], [2, 3, 'P2'], [3, 4, 'P3']]
    time_quantum = 2
    roundRobin(process_list, time_quantum)
