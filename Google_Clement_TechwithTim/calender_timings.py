schedule1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
constraint1 = ['09:00', '20:00']
schedule2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
constraint2 = ['10:00', '18:30']
meeting_time = 30
output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


def convert_times(times):
    start_time, end_time = times
    start_str, end_str = start_time.split(':'), end_time.split(':')
    start = int(start_str[0]) + int(start_str[1])/60
    end = int(end_str[0]) + int(end_str[1])/60
    return start, end


def larger_time(time1, time2):
    # returns the time that is larger
    t1, t2 = convert_times([time1, time2])
    return True if t1 >= t2 else False


def generate_limits(c1, c2):
    st1, end1 = convert_times(c1)
    st2, end2 = convert_times(c2)
    start_limit = c1[0] if st1 >= st2 else c2[0]
    end_limit = c1[1] if end1 <= end2 else c2[1]
    return [start_limit, end_limit]


def merge_intervals(flist, limits):
    merged = []
    merged.append(flist[0])
    for i in range(len(flist)):
        curr_begin, curr_end = merged[-1][0], merged[-1][1]
        next_begin, next_end = flist[i][0], flist[i][1]
        if larger_time(curr_end, next_begin):
            merged[-1][1] = next_end if larger_time(next_end, curr_end) else curr_end
        else:
            merged.append(flist[i])
    return merged


def check_difference(time1, time2, meeting_time):
    t1, t2 = convert_times([time1, time2])
    if t1 - t2 >= meeting_time/60:
        return True
    else:
        return False


def check_intervals(times, limits, meeting_time):
    final = []
    if check_difference(times[0][0], limits[0], meeting_time):  # time before first meeting
        final.append([limits[0], times[0][0]])
    for i in range(len(times)-1):
        curr_end, next_begin = times[i][1], times[i+1][0]
        if check_difference(next_begin, curr_end, meeting_time):  # time after a meeting
            final.append([curr_end, next_begin])
    if check_difference(limits[1], times[-1][1], meeting_time):  # time after last meeting
        final.append([times[-1][1], limits[1]])
    return final


def main():
    final_list = schedule1 + schedule2
    final_list.sort(key=convert_times)
    limits = generate_limits(constraint1, constraint2)
    merged_interval = merge_intervals(final_list, limits)
    final_list = check_intervals(merged_interval, limits, meeting_time)
    print(final_list)
    return final_list


assert main() == output
