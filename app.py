import streamlit as st
import pandas as pd

data = pd.read_json('queries.json')

queries = data.queries

query_list = []
org_list = {}
chart_dict = {}
columns = ["Keyword", "Phrase", "Relevance"]


for i in queries:
	# st.write(i)
	query = i["query"]
	query_list.append(query)
	response = i["response"]

	org_list[query] = []
	chart_dict[query] = {}

	org_avg = {}

	for res in response:
		org = res[1]
		val = res[3]
		if org in org_list[query]:
			org_avg[org].append(res[3])
			continue
		else:
			org_list[query].append(org)
			chart_dict[query][org] = 0
			org_avg[org] = [res[3]]

	# st.write(org_list)
	for org in org_list[query]:
		# st.write(org_avg[org])
		chart_dict[query][org] = sum(org_avg[org])/len(org_avg[org])


query_selected = st.selectbox('Select query', options = query_list)
org_selected = st.selectbox('Select org', options = org_list[query_selected])


query_index = query_list.index(query_selected)
row_list = []


chart_df = pd.DataFrame(chart_dict[query_selected].values(), index=chart_dict[query_selected].keys())


st.line_chart(chart_df)




for i in queries[query_index]["response"]:
	if(i[1] == org_selected):
		this_dict = {"Keyword": i[0], "Phrase": i[2], "Relevance": i[3]}
		row_list.append(this_dict)

selected_df = pd.DataFrame(row_list, columns = columns)

st.dataframe(selected_df)


