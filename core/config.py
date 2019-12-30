
LWM_INSERTION = 1
LWM_MERGE = 2
LWM_LINEAR = 3
LWM_MEDIAN_APPROX = 4
LWM = 5
exec_function = 2  # define the function that will be executed

debug_en = False  # print info data
debug_time = True


def debug_check():
    if debug_en:
        print('Warning debug is enabled in main code!\nGo to core/config.py to disable it.')

    if debug_time:
        print('Warning debug is enabled in time calculation!\nGo to core/config.py to disable it.')


execute_time_calculation = False  # execute also the time calculation

t_start_value = 1000
t_increment = 1000
t_max_value = 31000
