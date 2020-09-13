import asyncio

async def rng_1():
    for i in range(10):
        print(i)

async def rng_2():
    for b in range(7):
        print(b)

# rng_map = asyncio.gather(rng_1, rng_2)
asyncio.run(rng_2())