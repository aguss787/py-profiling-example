import asyncio
from math import floor
from line_profiler_pycharm import profile
from func.heavy_computation import slow_generate_prime, generate_prime
from func.io_operation import blocking, non_blocking


@profile
def run():
    n = 10000

    t = 0
    for i in range(floor(n ** 1.5)):
        t += i * i

    slow_generate_prime(n)
    generate_prime(n)


@profile
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
    asyncio.get_event_loop().run_until_complete(run_async())
