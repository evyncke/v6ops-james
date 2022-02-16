#!/usr/bin/env python3

import json


print('|AS Number|AS Description|')
all_as = json.load(open('analysed_as.json'))
for asn in all_as:
	print('|', asn['asn'], '|', asn['asn_description'], '|')
