import time


def calc_time(func):
    def clac(*args, **kwargs):
        start: float = time.perf_counter_ns()
        func(*args, **kwargs)
        end: float = time.perf_counter_ns()
        print(f'共用时间：{end - start}ns')

    return clac
