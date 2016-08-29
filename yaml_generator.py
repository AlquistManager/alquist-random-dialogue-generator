from random import randint
from yaml_templates import *
from config import *




def generate_demo():
    flow = open('yaml/demo_main.yml', 'w')
    flow.write(flow_start('demo_main'))
    flow.write(message_text('init', 'Hi, can I ask you a question?'))
    flow.write(input_user('user_yes', {'yes_no': 'yes_no'}, False, True, {'match': 'yes_no', 'notmatch': 'error_yes'}))
    flow.write(message_text('error_yes', 'Sorry, I don\'t understand, yes or no?', {'next_state': 'user_yes'}))
    flow.write(conditional_equal('yes_no', '{{yes_no}}', 'yes', {'equal': 'ask_number', 'notequal': 'bye'}))
    flow.write(input_context('debug_recent', {'number': 'number'}, {'flow': 'demo_second'}))
    flow.write(message_text_random('bye', ['OK, bye','I see, it was nice talking to you anyway','Oh, that is a shame, bye then']))


    flow = open('yaml/demo_second.yml', 'w')
    flow.write(flow_start('demo_second'))
    flow.write(conditional_exists('has_number', '{{number}}', {'exists': 'number_echo', 'notexists': 'leave_in_shame'}))
    flow.write(message_text('ask_number', 'What is your favourite number?'))
    flow.write(input_user('answer_number', {'number': 'number'}, True, True, {'match': 'debug_recent', 'notmatch': 'error_number'}))
    flow.write(message_text('error_number', 'I don\'t think that is a number. Try another one?', {'next_state': 'answer_number'}))
    flow.write(message_text('number_echo', 'Wow, {{number}}, really? That is super cool.', 'end'))
    flow.write(message_text('leave_in_shame', 'Well, this is awkward. \\nI seem to have forgotten your favourite number. \\nI am ... gonna ... go now. Bye', 'end'))


def generate_control_files():
    flow = open('yaml/gen_test.yml', 'w')
    flow.write(node_text(1, 'default'))
    flow.write(node_text(2, 'end'))
    flow.write(node_text(3, 1))
    flow.write(node_text(4, 'flow', 1))

    flow = open('yaml/gen_test_ran.yml', 'w')
    flow.write(node_random_text(1, 'default'))
    flow.write(node_random_text(2, 'end'))
    flow.write(node_random_text(3, 1))
    flow.write(node_random_text(4, 'flow', 1))

    flow = open('yaml/gen_test_eq.yml', 'w')
    flow.write(node_conditional_equal(1, 'ent1', 'ent2', 'end', 1))
    flow.write(node_conditional_equal(2, 'ent1', 'ent2', 'flow', 'end', flow1=1))
    flow.write(node_conditional_equal(3, 'ent1', 'ent2', 'flow', 'flow', flow1=3, flow2=4))
    flow.write(node_conditional_equal(4, 'ent1', 'ent2', 3, 'flow', flow2=2))

    flow = open('yaml/gen_test_ex.yml', 'w')
    flow.write(node_conditional_exists(1, 'key', 'end', 1))
    flow.write(node_conditional_exists(2, 'key', 'flow', 'end', flow1=1))
    flow.write(node_conditional_exists(3, 'key', 'flow', 'flow', flow1=3, flow2=4))
    flow.write(node_conditional_exists(4, 'key', 3, 'flow', flow2=2))

    flow = open('yaml/gen_test_inm.yml', 'w')
    flow.write(node_input_user_match(1, {'ent': 'ent', 'two': 'e2'}, 'end', 1))
    flow.write(node_input_user_match(2, {'ent': 'ent', 'two': 'e2'}, 'flow', 'end', flow1=1))
    flow.write(node_input_user_match(3, {'ent': 'ent', 'two': 'e2'}, 'flow', 'flow', flow1=3, flow2=4))
    flow.write(node_input_user_match(4, {'ent': 'ent', 'two': 'e2'}, 3, 'flow', flow2=2))

    flow = open('yaml/gen_test_inp.yml', 'w')
    flow.write(node_input_user_pass(1, {'ent': 'ent', 'two': 'e2'}, 'end'))
    flow.write(node_input_user_pass(2, {'ent': 'ent', 'two': 'e2'}, 'flow', 1))
    flow.write(node_input_user_pass(3, {'ent': 'ent', 'two': 'e2'}, 'default'))
    flow.write(node_input_user_pass(4, {'ent': 'ent', 'two': 'e2'}, 3))

    flow = open('yaml/gen_test_cx.yml', 'w')
    flow.write(node_input_context(1, {'ent': 'ent', 'two': 'e2'}, 'end'))
    flow.write(node_input_context(2, {'ent': 'ent', 'two': 'e2'}, 'flow', 1))
    flow.write(node_input_context(3, {'ent': 'ent', 'two': 'e2'}, 'default'))
    flow.write(node_input_context(4, {'ent': 'ent', 'two': 'e2'}, 3))


def write_flow(filename, first_id, last_id, order):
    flow = open(filename, 'w')
    flow.write(flow_start('flow_1'))
    for i in range(first_id, last_id):
        n = order[i]
        print("i = " + str(i) + 'n = ' + str(n))
        tr_id1 = randint(0, 20)
        tr_id2 = randint(0, 20)
        if n < COND_EQ_NODES:

            flow_tr_1 = randint(0, 4)
            flow_tr_2 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)
            if tr_id2 == 0:
                trans2 = 'end'
            elif tr_id2 == 1:
                trans2 = 'flow'
            else:
                trans2 = randint(0, TOTAL_NODES - 1)
            e1 = randint(0, 4)
            e2 = randint(0, 4)
            if e1 == 0:
                entity1 = '{{num1}}'
            elif e1 == 1:
                entity1 = '{{num2}}'
            elif e1 == 2:
                entity1 = '{{num3}}'
            elif e1 == 3:
                entity1 = '0'
            else:
                entity1 = '1'
            if e2 == 0:
                entity2 = '{{num1}}'
            elif e2 == 1:
                entity2 = '{{num2}}'
            elif e2 == 2:
                entity2 = '{{num3}}'
            elif e2 == 3:
                entity2 = '0'
            else:
                entity2 = '1'
            flow.write(node_conditional_equal(i, entity1, entity2, trans1, trans2, flow_tr_1, flow_tr_2))
        elif n < COND_EX_NODES + COND_EQ_NODES:

            flow_tr_1 = randint(0, 4)
            flow_tr_2 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)
            if tr_id2 == 0:
                trans2 = 'end'
            elif tr_id2 == 1:
                trans2 = 'flow'
            else:
                trans2 = randint(0, TOTAL_NODES - 1)
            e1 = randint(0, 2)
            if e1 == 0:
                entity1 = '{{num1}}'
            elif e1 == 1:
                entity1 = '{{num2}}'
            else:
                entity1 = '{{num3}}'
            flow.write(node_conditional_exists(i, entity1, trans1, trans2, flow_tr_1, flow_tr_2))
        elif n < COND_EX_NODES + COND_EQ_NODES + UI_MATCH_NODES:

            flow_tr_1 = randint(0, 4)
            flow_tr_2 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)
            if tr_id2 == 0:
                trans2 = 'end'
            elif tr_id2 == 1:
                trans2 = 'flow'
            else:
                trans2 = randint(0, TOTAL_NODES - 1)
            e1 = randint(0, 4)
            if e1 == 0:
                entities = {'num1': 'number'}
            elif e1 == 1:
                entities = {'num2': 'number'}
            elif e1 == 2:
                entities = {'num3': 'number'}
            elif e1 == 3:
                entities = {'num1': 'number', 'num3': 'number'}
            else:
                entities = {'num1': 'number', 'num2': 'number', 'num3': 'number'}
            flow.write(node_input_user_match(i, entities, trans1, trans2, flow_tr_1, flow_tr_2))
        elif n < COND_EX_NODES + COND_EQ_NODES + UI_MATCH_NODES + UI_PASS_NODES:

            flow_tr_1 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            elif tr_id1 < 6:
                trans1 = 'default'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)

            e1 = randint(0, 4)
            if e1 == 0:
                entities = {'num1': 'number'}
            elif e1 == 1:
                entities = {'num2': 'number'}
            elif e1 == 2:
                entities = {'num3': 'number'}
            elif e1 == 3:
                entities = {'num1': 'number', 'num3': 'number'}
            else:
                entities = {'num1': 'number', 'num2': 'number', 'num3': 'number'}
            flow.write(node_input_user_pass(i, entities, trans1, flow_tr_1))
        elif n < COND_EX_NODES + COND_EQ_NODES + UI_MATCH_NODES + UI_PASS_NODES + CONTEXT_NODES:

            flow_tr_1 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            elif tr_id1 < 6:
                trans1 = 'default'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)

            e1 = randint(0, 4)
            if e1 == 0:
                entities = {'num1': 'number'}
            elif e1 == 1:
                entities = {'num2': 'number'}
            elif e1 == 2:
                entities = {'num3': 'number'}
            elif e1 == 3:
                entities = {'num1': 'number', 'num3': 'number'}
            else:
                entities = {'num1': 'number', 'num2': 'number', 'num3': 'number'}
            flow.write(node_input_context(i, entities, trans1, flow_tr_1))
        elif n < COND_EX_NODES + COND_EQ_NODES + UI_MATCH_NODES + UI_PASS_NODES + CONTEXT_NODES + RANDOM_NODES:

            flow_tr_1 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            elif tr_id1 < 6:
                trans1 = 'default'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)
            flow.write(node_random_text(i, trans1, flow_tr_1))
        else:

            flow_tr_1 = randint(0, 4)

            if tr_id1 == 0:
                trans1 = 'end'
            elif tr_id1 == 1:
                trans1 = 'flow'
            elif tr_id1 < 6:
                trans1 = 'default'
            else:
                trans1 = randint(0, TOTAL_NODES - 1)
            flow.write(node_text(i, trans1, flow_tr_1))








