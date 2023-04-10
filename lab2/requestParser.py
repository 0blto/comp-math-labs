def parse_equation(content):
    return content['equation'], content['method'], \
        content['left'], content['right'], \
        content['epsilon']


def parse_system(content):
    return content['system'], \
           content['left'], content['right'], \
           content['epsilon']

def parse_equation_result(content):
    return content['equation'], \
           content['root'], content['start'], \
           content['end']

def parse_system_plt(content):
    return content['system'], \
           content['x'], content['y']
