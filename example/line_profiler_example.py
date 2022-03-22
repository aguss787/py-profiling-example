import asyncio
from math import floor
from line_profiler import line_profiler
from func.heavy_computation import slow_generate_prime, generate_prime
from func.io_operation import io_ops, blocking, non_blocking

lp = line_profiler.LineProfiler()


@lp
def run():
    n = 10000

    t = 0
    for i in range(floor(n ** 1.5)):
        t += i * i

    slow_generate_prime(n)
    generate_prime(n)


@lp
async def run_async():
    n = 10000

    t = 0
    for i in range(floor(n ** 1.5)):
        t += i * i

    blocking(1)
    await non_blocking(1)
    blocking(1)
    await non_blocking(1)


if __name__ == '__main__':
    run()

    lp.add_function(io_ops)
    asyncio.get_event_loop().run_until_complete(io_ops())
    asyncio.get_event_loop().run_until_complete(run_async())

    lp.print_stats()

