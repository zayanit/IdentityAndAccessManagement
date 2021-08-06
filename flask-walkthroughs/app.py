from flask import Flask, request, abort

def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)

    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')

    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401)

    return header_parts[1]

app = Flask(__name__)

@app.route('/headers')
def headers():
    # @TODO unpack the request header
    jwt = get_token_auth_header()
    print(jwt)
    return 'not umplemented'