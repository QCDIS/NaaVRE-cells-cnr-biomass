
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--outputs', action='store', type=str, required=True, dest='outputs')


args = arg_parser.parse_args()
print(args)

id = args.id

outputs = args.outputs.replace('"','')




outputs['nome'] = 'TEST'

