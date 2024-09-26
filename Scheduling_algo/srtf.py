# Shortest roundtrip first (sjf preemtive)
# burst is significant to its placed at first position
# processlist = [BT,AT,PIT]

def sjf_preemptive(process_list):
    t = 0
    # for logging each process execution orderly
    gantt = []
    # to track completed processes
    completed = {}

    # storing BT of processes for calculation of WT
    burst_time = {}
    for i in process_list:
        burst_time[i[2]] = i[0]

    while process_list:
        # proceess that has arrived
        available = [p for p in process_list if p[1]<=t]

        # if no process has arrived
        if not available:
            t += 1
            gantt.append("idle")
            continue
        else:
            # sorting for smallest BT
            available.sort()
            process = available.pop(0)
            # removing from the process List 
            process_list.remove(process)

            # now servicing the process for only a unit
            # so that we can check whether new processe with smaller BT has arrived or not
            t += 1
            gantt.append(process[2])
            # decreasing the process BT
            process[0] -= 1

            # process is completed then we are not queueing it anymore
            if(process[0] == 0):
                pid = process[2]
                ct = t
                bt = burst_time[pid]
                tt = ct - process[1]
                wt = tt - bt

                completed[pid] = [ct,tt,wt]
                continue
            else:
                # queuing it again
                process_list.append(process)

    print(gantt)
    print(completed)


if __name__ == '__main__':
    process_list = [[2, 0, 'P1'], [3, 2, 'P2'], [1, 4, 'P3']]
    sjf_preemptive(process_list)