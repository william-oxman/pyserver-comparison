from fastapi import FastAPI

from src.fastapi_app.utils import datastore


app = FastAPI()


@app.on_event('startup')
async def starup_event():
    await datastore.init_redis('redis://127.0.0.1:6379')


@app.get('/example')
async def get():
    '''
    for this example, assume redis only holds the value for key 'shallow',
    where mongo only holds the key 'deep' and each of these values has some
    key 'foo'
    :return:
    '''
    deep = await datastore.get('deep')
    shallow = await datastore.get('shallow')
    return f"deep: {deep['foo']}, shallow: {shallow['foo']}"
