import asyncio
from time import time

import click

from scripts import stress_test


@click.command()
@click.option('--server', default='UNSUPPLIED', help='Server type, e.g. Gunicorn/Flask')
@click.option('--port', default=8080, help='Server port')
def main(server, port):
    t0 = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(stress_test.main(f'http://0.0.0.0:{port}/example'))
    t1 = time()
    print(f'{server} completed 10000 requests in {t1 - t0} seconds')


if __name__ == '__main__':
    main()
