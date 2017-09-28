from pythonosc import udp_client, osc_message_builder

from flask import Flask
from flask import request
from flask import render_template

# See if using gevent monkey patching helps with latency
# from gevent import monkey
# monkey.patch_socket()


app = Flask(__name__)

client = udp_client.UDPClient('localhost', 8000)


def send_msg(addr, args=[]):
    msg = osc_message_builder.OscMessageBuilder(address=addr)
    for arg in args:
        msg.add_arg(arg)
    built_msg = msg.build()
    client.send(built_msg)
    


@app.route("/")
def index():
    return render_template('page.html')



@app.route("/axis/")
def hello():
    a = request.args.get('a')
    b = request.args.get('b')
    g = request.args.get('g')
    
    # print(a, b, g)

    send_msg("/renoise/song/track/5/device/2/set_parameter_by_index", [2, float(a)/360 ])
    send_msg("/renoise/song/track/5/device/2/set_parameter_by_index", [3, float(b)/180 ])
    return "Hello World!" + a

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
