#!/usr/bin/env python3

import json

def get_asn(a):
	return int(a['asn'])

print('|AS Number|AS Description|')
all_as = json.load(open('analysed_as.json'))
all_as.sort(key = get_asn)
for asn in all_as:
	print('|', asn['asn'], '|', asn['asn_description'], '|')
