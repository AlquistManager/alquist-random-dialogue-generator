import os
from random import shuffle

from config import *
from yaml_generator import write_flow
from yaml_templates import flow_start, message_text



if __name__ == '__main__':
    if not os.path.exists('yaml/'):
        os.makedirs('yaml/')

    ordered = [i for i in range(100)]
    shuffle(ordered)
    flow = open('yaml/flow.yml', 'w')
    flow.write(flow_start('flow'))
    flow.write(message_text('init', 'INITIAL STATE', {'flow': 'flow_0'}))
    write_flow('yaml/flow_0.yml', 0, int(TOTAL_NODES/5), ordered)
    write_flow('yaml/flow_1.yml', int(TOTAL_NODES/5), int(TOTAL_NODES/5*2), ordered)
    write_flow('yaml/flow_2.yml', int(TOTAL_NODES/5*2), int(TOTAL_NODES/5*3), ordered)
    write_flow('yaml/flow_3.yml', int(TOTAL_NODES/5*3), int(TOTAL_NODES/5*4), ordered)
    write_flow('yaml/flow_4.yml', int(TOTAL_NODES/5*4), int(TOTAL_NODES), ordered)