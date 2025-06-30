
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output', action='store', type=str, required=True, dest='output')


args = arg_parser.parse_args()
print(args)

id = args.id

output = args.output.replace('"','')




output['nome'] = 'TEST'

