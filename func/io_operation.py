import asyncio
import time


def blocking(secs: float = 1.0) -> None:
    time.sleep(secs)


async def non_blocking(secs: float = 1.0) -> None:
    await asyncio.sleep(secs)


async def io_ops():
    blocking(1)
    await non_blocking(1)
    blocking(1)
    await non_blocking(1)
