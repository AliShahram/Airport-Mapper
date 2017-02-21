#!/usr/bin/env python3

from json import dumps
import pandas as pd


def file_import(input_file):
	source_point, dest_point, value = "Source", "Destination", "Value"
	nodes_set, links, nodes_list = set(), list(), list()

	# Helper methods
	def mapper(u):
		return list(nodes_set).index(u)

	def nodes_create(x):
		nodes_set.add(x[source_point])
		nodes_set.add(x[dest_point])

	def links_create(x):
		links.append({
			'source': mapper(x[source_point]),
			'target': mapper(x[dest_point]),
			'value': x[value]
		})

	def links_num(x):
		indexes = [mapper(x[source_point]), mapper(x[dest_point])]
		for index in indexes:
			nodes_list[index]['num_links'] += 1

	# Reading in file
	df = pd.read_csv(input_file)
	df.drop(df.columns[[0]], axis=1, inplace=True)

	df.apply(nodes_create, axis=1)
	df.apply(links_create, axis=1)

	nodes_list = list(nodes_set)
	for i in range(len(nodes_list)):
		nodes_list[i] = {'name': nodes_list[i], 'num_links': 0}

	df.apply(links_num, axis=1)

	final = {'nodes': nodes_list, 'links': links}

	return dumps(final, indent=4, sort_keys=True)
