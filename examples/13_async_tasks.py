"""Demonstrate concurrency with simulated I/O, without network access."""

import asyncio


async def prepare(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}: ready"


async def prepare_all() -> list[str]:
    # gather returns results in input order, even if completion order differs.
    return await asyncio.gather(prepare("report", 0.02), prepare("summary", 0.01))


def main() -> None:
    for result in asyncio.run(prepare_all()):
        print(result)


if __name__ == "__main__":
    main()
