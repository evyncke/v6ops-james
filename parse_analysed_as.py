#!/usr/bin/env python3

import json

# From https://en.wikipedia.org/wiki/Tier_1_network#cite_note-11

tier1 = {174, 7018, 3320, 3257, 6830, 3356, 2914, 5511, 3491, 1239, 6453, 6762, 1299, 12956, 701, 6461 }
regional_tier = {4134, 4809, 7473, 7922, 6939, 9002, 1273, 2828, 4637 }
 
def get_asn(a):
	return int(a['asn'])

print('|AS Number|AS Description|Comment|')
all_as = json.load(open('analysed_as.json'))
all_as.sort(key = get_asn)
for asn in all_as:
	comment = ''
	if int(asn['asn']) in tier1:
		comment = 'Tier-1'
	elif int(asn['asn']) in regional_tier:
		comment = 'Regional Tier'
	print('|', asn['asn'], '|', asn['asn_description'], '|',comment,'|')
