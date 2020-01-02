#!/usr/bin/env python3

import sys
# from functions import Task


HELP_MESSAGE = """USAGE
\t./307multigrains n1 n2 n3 n4 po pw pc pb ps

DESCRIPTION
\t n1 \t number of tons of fertilizer F1
\t n2 \t number of tons of fertilizer F2
\t n3 \t number of tons of fertilizer F3
\t n4 \t number of tons of fertilizer F4
\t po \t price of one unit of oat
\t pw \t price of one unit of wheat
\t pc \t price of one unit of corn
\t pb \t price of one unit of barley
\t ps \t price of one unit of soy
"""


def help():
    return HELP_MESSAGE


def error(message):
    sys.stderr.write(message+'\n')
    sys.exit(84)


# def parse_tasks(filename):
#     tasks = []
#     with open(filename) as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 error('Task line is empty.')
#             tokens = line.split(';')
#             if len(tokens) < 3:
#                 error('Not enough task information: {}'.format(tokens))
#             task_id, description, duration, predecesors = *tokens[:3], tokens[3:]
#             try:
#                 duration = int(duration)
#             except ValueError:
#                 error('Could not parse the duration field as a number.')
#             if duration < 0:
#                 error('Duration is negative: %d' % duration)
#             et=0
#             lt=0
#             successors=[]

#             #task = Task(task_id, description, duration, predecesors)
#             task = Task(task_id, description, duration, predecesors,et,lt,successors)
#             tasks.append(task)
#     return tasks
