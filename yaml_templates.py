def flow_start(name):
    return 'name: ' + name + '\rstates:\r'

#
# Generates message text state block
#
def node_text(num, next_num, flow=None):
    if next_num == 'default':
        return message_text('node_' + str(num),
                            'Accessing node ' + str(num) + '. This is a message_text node. This node is output only. Node ' +
                            str(num + 1) + ' follows.', next_num)
    elif next_num == 'end':
        return message_text('node_' + str(num),
                            'Accessing node ' + str(num) + '. This is a message_text node. This node is output only. This is an END node.',
                            str(next_num))
    elif next_num == 'flow':
        return message_text('node_' + str(num),
                            'Accessing node ' + str(num) + '. This is a message_text node. This node is output only. Flow ' + str(flow) + ' follows.',
                            {'flow': 'flow_' + str(flow)})
    else:
        return message_text('node_' + str(num),
                            'Accessing node ' + str(num) + '. This is a message_text node. This node is output only. Node ' + str(next_num) + ' follows.',
                            {'next_state': 'node_' + str(next_num)})


#
# Generates message random text state block
#
def node_random_text(num, next_num, flow=None):
    if next_num == 'default':
        return message_text_random('node_' + str(num), [
            'RESPONSE 1. Accessing node ' + str(num) + '. This is a message_text_random node. This node is output only. Node ' + str(
                num + 1) + ' follows.',
            'RESPONSE 2. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(
                num + 1) + ' follows.',
            'RESPONSE 3. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(
                num + 1) + ' follows.',
            'RESPONSE 4. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(
                num + 1) + ' follows.',
            'RESPONSE 5. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(
                num + 1) + ' follows.'],
                                   str(next_num))
    elif next_num == 'end':
        return message_text_random('node_' + str(num), [
            'RESPONSE 1. Accessing node ' + str(num) + '. This is a message_text_random node. This node is output only. This is an END node',
            'RESPONSE 2. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. This is an END node',
            'RESPONSE 3. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. This is an END node',
            'RESPONSE 4. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. This is an END node',
            'RESPONSE 5. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. This is an END node'],
                                   str(next_num))

    elif next_num == 'flow':
        return message_text_random('node_' + str(num), [
            'RESPONSE 1. Accessing node ' + str(num) + '. This is a message_text_random node. This node is output only. Flow ' + str(flow) + ' follows.',
            'RESPONSE 2. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Flow ' + str(flow) + ' follows.',
            'RESPONSE 3. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Flow ' + str(flow) + ' follows.',
            'RESPONSE 4. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Flow ' + str(flow) + ' follows.',
            'RESPONSE 5. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Flow ' + str(flow) + ' follows.'],
                                   {'flow': 'flow_' + str(flow)})
    else:
        return message_text_random('node_' + str(num), [
            'RESPONSE 1. Accessing node ' + str(num) + '. This is a message_text_random node. This node is output only. Node ' + str(next_num) + ' follows.',
            'RESPONSE 2. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(next_num) + ' follows.',
            'RESPONSE 3. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(next_num) + ' follows.',
            'RESPONSE 4. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(next_num) + ' follows.',
            'RESPONSE 5. Accessing node ' + str(num) + '. This is an message_text_random node. This node is output only. Node ' + str(next_num) + ' follows.'],
                                   {'next_state': 'node_' + str(next_num)})


#
# Generates conditional_equal node block
#
def node_conditional_equal(num, entity1, entity2, next1, next2, flow1=None, flow2=None):
    text = message_text('node_' + str(num),
                        'Accessing node ' + str(num) + '. This is a conditional_equal node. This node compares ' + entity1 + ' and ' + entity2 + ' This node is output only.', {'next_state': 'node_' + str(num) + '_exec'})
    exec = conditional_equal('node_' + str(num) + '_exec', entity1, entity2,
                             {'equal': 'node_' + str(num) + '_pass', 'notequal': 'node_' + str(num) + '_fail'})

    if next1 == 'end':
        pass_ = message_text('node_' + str(num) + '_pass',
                            'PASS. This is an END node',
                            str(next1))
    elif next1 == 'flow':
        pass_ = message_text('node_' + str(num) + '_pass',
                            'PASS. Flow ' + str(flow1) + ' follows.',
                            {'flow': 'flow_' + str(flow1)})
    else:
        pass_ = message_text('node_' + str(num) + '_pass',
                            'PASS. Node ' + str(next1) + ' follows.',
                            {'next_state': 'node_' + str(next1)})


    if next2 == 'end':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. This is an END node',
                             str(next2))
    elif next2 == 'flow':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Flow ' + str(flow2) + ' follows.',
                            {'flow': 'flow_' + str(flow2)})
    else:
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Node ' + str(next2) + ' follows.',
                            {'next_state': 'node_' + str(next2)})

    return text + exec + pass_ + fail


#
# Generates conditional_exisis node block
#
def node_conditional_exists(num, key, next1, next2, flow1=None, flow2=None):
    text = message_text('node_' + str(num),
                        'Accessing node ' + str(num) + '. This is a conditional_equal node. THis node checks, if entity ' + key + ' exists. This node is output only.', {'next_state': 'node_' + str(num) + '_exec'})
    exec = conditional_exists('node_' + str(num) + '_exec', key,
                             {'exists': 'node_' + str(num) + '_pass', 'notexists': 'node_' + str(num) + '_fail'})

    if next1 == 'end':
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. This is an END node',
                             str(next1))
    elif next1 == 'flow':
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. Flow ' + str(flow1) + ' follows.',
                             {'flow': 'flow_' + str(flow1)})
    else:
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. Node ' + str(next1) + ' follows.',
                             {'next_state': 'node_' + str(next1)})

    if next2 == 'end':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. This is an END node',
                            str(next2))
    elif next2 == 'flow':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Flow ' + str(flow2) + ' follows.',
                            {'flow': 'flow_' + str(flow2)})
    else:
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Node ' + str(next2) + ' follows.',
                            {'next_state': 'node_' + str(next2)})

    return text + exec + pass_ + fail

#
# Generates input_user node block with matching
#
def node_input_user_match(num, entities, next1, next2, flow1=None, flow2=None):
    text = message_text('node_' + str(num),
                        'Accessing node ' + str(num) + '. This is a input_user node. This is an INPUT node. This node requires enitiy match.' , {'next_state': 'node_' + str(num) + '_exec'})
    exec = input_user('node_' + str(num) + '_exec', entities, True, True,
                             {'match': 'node_' + str(num) + '_pass', 'notmatch': 'node_' + str(num) + '_fail'})

    if next1 == 'end':
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. This is an END node',
                             str(next1))
    elif next1 == 'flow':
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. Flow ' + str(flow1) + ' follows.',
                             {'flow': 'flow_' + str(flow1)})
    else:
        pass_ = message_text('node_' + str(num) + '_pass',
                             'PASS. Node ' + str(next1) + ' follows.',
                             {'next_state': 'node_' + str(next1)})

    if next2 == 'end':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. This is an END node',
                            str(next2))
    elif next2 == 'flow':
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Flow ' + str(flow2) + ' follows.',
                            {'flow': 'flow_' + str(flow2)})
    else:
        fail = message_text('node_' + str(num) + '_fail',
                            'FAIL. Node ' + str(next2) + ' follows.',
                            {'next_state': 'node_' + str(next2)})

    return text + exec + pass_ + fail


#
# Generates input_user node block without matching
#
def node_input_user_pass(num, entities, next_num, flow=None):
    text = message_text('node_' + str(num),
                        'Accessing node ' + str(num) + '. This is a input_user node. This is an INPUT node. This node does NOT require enitiy match.', {'next_state': 'node_' + str(num) + '_exec'})
    exec = input_user('node_' + str(num) + '_exec', entities, True, False,
                             {'next_state': 'node_' + str(num) + '_end'})

    if next_num == 'default':
        end =  message_text('node_' + str(num) + '_end',
                            'Input recieved. Node ' +
                            str(num + 1) + ' follows.',
                            str(next_num))
    elif next_num == 'end':
        end = message_text('node_' + str(num) + '_end',
                             'Input recieved. This is an END node',
                           str(next_num))
    elif next_num == 'flow':
        end = message_text('node_' + str(num) + '_end',
                             'Input recieved. Flow ' + str(flow) + ' follows.',
                             {'flow': 'flow_' + str(flow)})
    else:
        end = message_text('node_' + str(num) + '_end',
                             'Input recieved. Node ' + str(next_num) + ' follows.',
                           {'next_state': 'node_' + str(next_num)})

    return text + exec + end

#
# Generates input_user node block without matching
#
def node_input_context(num, entities, next_num, flow=None):
    text = message_text('node_' + str(num),
                        'Accessing node ' + str(num) + '. This is a input_context node. This is an output node. This node does NOT require enitiy match.', {'next_state': 'node_' + str(num) + '_exec'})
    exec = input_context('node_' + str(num) + '_exec', entities,
                             {'next_state': 'node_' + str(num) + '_end'})

    if next_num == 'default':
        end = message_text('node_' + str(num) + '_end',
                            'Context loaded. Node ' +
                            str(num + 1) + ' follows.',
                            str(next_num))
    elif next_num == 'end':
        end = message_text('node_' + str(num) + '_end',
                             'Context loaded. This is an END node',
                           str(next_num))
    elif next_num == 'flow':
        end = message_text('node_' + str(num) + '_end',
                             'Context loaded.' + str(flow) + 'follows.',
                             {'flow': 'flow_' + str(flow)})
    else:
        end = message_text('node_' + str(num) + '_end',
                             'Context loaded. Node ' + str(next_num) + ' follows.',
                           {'next_state': 'node_' + str(next_num)})

    return text + exec + end



# Generators for individual state types follow
def message_text(name, text, transitions='default'):
    tmp_yml = '  ' + name + ':\r    type: message_text\r    properties:\r      text: ' + text + '\r'
    if transitions == 'end':
        tmp_yml = tmp_yml + '    transitions:\r      next_state:\r'
    elif transitions != 'default':
        tmp_yml = tmp_yml + '    transitions:\r'
        for transition in transitions:
            tmp_yml = tmp_yml + '      ' + str(transition) + ': ' + str(transitions[transition]) + '\r'
    return tmp_yml + '\r'


def message_text_random(name, responses, transitions='default'):
    tmp_yml = '  ' + name + ':\r    type: message_text_random\r    properties:\r      responses:\r'
    for response in responses:
        tmp_yml = tmp_yml + '        - ' + response + '\r'
    if transitions == 'end':
        tmp_yml = tmp_yml + '    transitions:\r      next_state:\r'
    elif transitions != 'default':
        tmp_yml = tmp_yml + '    transitions:\r'
        for transition in transitions:
            tmp_yml = tmp_yml + '      ' + transition + ': ' + transitions[transition] + '\r'
    return tmp_yml + '\r'


def conditional_equal(name, val1, val2, transitions):
    tmp_yml = '  ' + name + ':\r    type: conditional_equal\r    properties:\r      value1: \'' + val1 + '\'\r      value2: \'' + val2 + '\'\r'
    tmp_yml = tmp_yml + '    transitions:\r'
    for transition in transitions:
        tmp_yml = tmp_yml + '      ' + transition + ': ' + transitions[transition] + '\r'
    return tmp_yml + '\r'


def conditional_exists(name, key, transitions):
    tmp_yml = '  ' + name + ':\r    type: conditional_exists\r    properties:\r      key: \'' + key + '\'\r'
    tmp_yml = tmp_yml + '    transitions:\r'
    for transition in transitions:
        tmp_yml = tmp_yml + '      ' + transition + ': ' + transitions[transition] + '\r'
    return tmp_yml + '\r'


def input_user(name, entities, log_json=False, require_match=False, transitions='default'):
    tmp_yml = '  ' + name + ':\r    type: input_user\r    properties:\r      entities:\r'
    for entity in entities:
        tmp_yml = tmp_yml + '        ' + entity + ': ' + entities[entity] + '\r'
    tmp_yml = tmp_yml + '      log_json: ' + str(log_json) + '\r      require_match: ' + str(require_match) + '\r'
    if require_match:
        tmp_yml = tmp_yml + '    transitions:\r      match: ' + transitions.get(
            'match') + '\r      notmatch: ' + transitions.get('notmatch') + '\r'
    else:
        if transitions == 'end':
            tmp_yml = tmp_yml + '    transitions:\r      next_state:\r'
        elif transitions != 'default':
            tmp_yml = tmp_yml + '    transitions:\r'
            for transition in transitions:
                tmp_yml = tmp_yml + '      ' + transition + ': ' + transitions[transition] + '\r'
    return tmp_yml + '\r'


def input_context(name, entities, transitions='default'):
    tmp_yml = '  ' + name + ':\r    type: input_context\r    properties:\r      entities:\r'
    for entity in entities:
        tmp_yml = tmp_yml + '        ' + entity + ': ' + entities[entity] + '\r'
    if transitions == 'end':
        tmp_yml = tmp_yml + '    transitions:\r      next_state:\r'
    elif transitions != 'default':
        tmp_yml = tmp_yml + '    transitions:\r'
        for transition in transitions:
            tmp_yml = tmp_yml + '      ' + transition + ': ' + transitions[transition] + '\r'
    return tmp_yml + '\r'
