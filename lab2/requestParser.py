def parse_equation(content):
    return content['equation'], content['method'], \
        content['left'], content['right'], \
        content['epsilon']


def parse_system(content):
    return content['system'], \
           content['left'], content['right'], \
           content['epsilon']
