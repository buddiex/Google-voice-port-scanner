from port_scanner import scanPorts
from flask import Flask, request, jsonify, make_response
# import dialogflow
from dotenv import load_dotenv
import logging, os, json

# load dotenv in the base root
basedir = os.path.abspath(".")
logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(basedir, 'test')),
        logging.StreamHandler()
    ],
    level=logging.DEBUG
)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
app = Flask(__name__)

#number to call +1 208-252-9201

@app.route("/process_intent", methods=['GET', 'POST'])
def process_intent():
    req = request.get_json(force=True)
    try:

        if req['queryResult']['intent']['displayName'] == 'external port scan':
                output = scan(req['queryResult']['parameters']['servername'])

        # if intent == 'Scan other Ports':
        #     output = scan('redis,database')

        res = {'fulfillmentText': output}

    except Exception as e:
        res = {'speech': 'error', 'displayText': 'Exception {}'.format(e)}

    return make_response(jsonify(res))


@app.route('/')
def index():
    servers = 'redis,localhost'
    return scan(servers)


def scan(address):
    result = scanPorts(address)
    text = ['Port{} {} {} open on {}'.format('' if len(p) == 1 else 's',
                                             ' '.join(p),
                                             'is' if len(p) == 1 else 'are',
                                             k)
            for k, p in result.items() if k != 'duration']
    return ', '.join(text)


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=8000, debug=True )


