from flask import Flask, jsonify

from src.flask_app.utils import datastore


app = Flask(__name__)


@app.route('/example')
def get_():
    '''
    for this example, assume redis only holds the value for key 'shallow',
    where mongo only holds the key 'deep' and each of these values has some
    key 'foo'
    :return:
    '''
    deep = datastore.get('deep')
    shallow = datastore.get('shallow')
    return jsonify(f"deep: {deep['foo']}, shallow: {shallow['foo']}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
