from enum import Enum
from functools import wraps
from math import floor
from pathlib import Path

import asyncio
import yappi

from func.heavy_computation import slow_generate_prime, generate_prime
from func.io_operation import io_ops


class ClockType(str, Enum):
    CPU = "cpu"
    WALL = "wall"


def yappi_profiled_async(prefix: str = "", clock_type: ClockType = ClockType.CPU):
    def decorator(f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            is_first = not yappi.is_running()

            if is_first:
                yappi.clear_stats()
                yappi.set_clock_type(clock_type.value)
                yappi.start()

            await f(*args, **kwargs)

            if is_first:
                yappi.stop()

            sep = '' if prefix == '' else '-'
            filename = f'output/callgrind.{prefix}{sep}func_state.prof'
            stats = yappi.get_func_stats()
            stats.save(filename, type='callgrind')
            stats.print_all()

        return wrapper

    return decorator


async def _run():
    n = 10000

    def cpu_heavy_thingy():
        t = 0
        for i in range(floor(n**1.5)):
            t += i * i

        slow_generate_prime(n)
        generate_prime(n)

    cpu_heavy_thingy()
    await io_ops()


@yappi_profiled_async(prefix="decorated_example")
async def decorated():
    await _run()


async def run():
    await decorated()
    await yappi_profiled_async(prefix="cpu", clock_type=ClockType.CPU)(_run)()
    await yappi_profiled_async(prefix="wall", clock_type=ClockType.WALL)(_run)()


def main():
    # Prepare output path
    Path('output').mkdir(exist_ok=True)

    asyncio.get_event_loop().run_until_complete(run())


if __name__ == '__main__':
    main()
