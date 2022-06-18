#!/usr/bin/env python3

import json
import re

# From https://en.wikipedia.org/wiki/Tier_1_network#cite_note-11

tier1 = {174, 7018, 3320, 3257, 6830, 3356, 2914, 5511, 3491, 1239, 6453, 6762, 1299, 12956, 701, 6461 }
regional_tier = {4134, 4809, 7473, 7922, 6939, 9002, 1273, 2828, 4637 }
 
def get_asn(a):
	return int(a['asn'])

# Input file is not really JSON...
raw_json_string = '[\n' + open('analysed_as.json').read().replace("'", '"').replace('}', '},')
final = -1 if raw_json_string[:-1] == ',' else -2 #take care of the last \n if any
raw_json_string = raw_json_string[:final] + ']\n'
raw_json_string = re.sub(r'\d+: ', '', raw_json_string)

all_as = json.loads(raw_json_string)
all_as.sort(key = get_asn)
print('|AS Number|AS Description|Comment|')
for asn in all_as:
	comment = ''
	if int(asn['asn']) in tier1:
		comment = 'Tier-1'
	elif int(asn['asn']) in regional_tier:
		comment = 'Regional Tier'
	print('|', asn['asn'], '|', asn['asn_description'], '|',comment,'|')
