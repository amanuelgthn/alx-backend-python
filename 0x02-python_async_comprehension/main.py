#!/usr/bin/env python3
"""Hello world """


import asyncio 

# couroutine function
async def main():
    print("Hello ................")
    await asyncio.sleep(1)
    print("...world!")

asyncio.run(main())