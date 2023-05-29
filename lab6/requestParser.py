def parse_request(content):
    return content['equation'], content['method'], \
        content['x'], content['y'], \
        content['epsilon'], content['len'], content['h']

