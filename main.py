import asyncio
from pathlib import Path

import example.yappi_example


def main():
    # Prepare output path
    Path('output').mkdir(exist_ok=True)

    asyncio.get_event_loop().run_until_complete(example.yappi_example.run())


if __name__ == '__main__':
    main()
