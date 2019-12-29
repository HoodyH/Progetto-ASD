
LWM_NAIVE = 1
LWM = 0
LWM_APPROX = 2
exec_function = 0  # define the function that will be executed

debug_en = True  # print info data


def debug_check():
    if debug_en:
        print('Warning debug is enabled!\nGo to core/config.py to disable it.')


execute_time_calculation = False  # execute also the time calculation

t_start_value = 1000
t_increment = 1000
t_max_value = 31000

execute_naive_lwm = True
execute_lwm = True
