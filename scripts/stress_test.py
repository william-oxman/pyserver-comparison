import asyncio

from aiohttp import ClientSession


# things get fishy around 16400 requests...
TOTAL_REQUESTS = 10000

COMPLETED = 0


async def get_example_data(session, url):
    """Get example data from a locally running API (asynchronously)"""
    try:
        response = await session.request(method='GET', url=url)
        if response.status > 299:
            print(f"HTTP error occurred: {response.status}")
        # track 200 response total
        global COMPLETED
        COMPLETED += 1
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json(content_type=None)
    return response_json


async def make_call(session, url):
    """Wrapper for running program in an asynchronous manner"""
    try:
        response = await get_example_data(session, url)
    except Exception as err:
        print(f"Exception occured: {err}")
        pass


async def main(url):
    semaphore = asyncio.Semaphore(64)
    async with semaphore:
        async with ClientSession(trust_env=True) as session:
            calls = [make_call(session, url) for i in range(TOTAL_REQUESTS)]
            await asyncio.gather(*calls)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main('0.0.0.0:8080/example'))
