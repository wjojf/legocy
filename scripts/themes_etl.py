import json 
import pandas as pd


SETS_FILEPATH = '..backend/static/json/lego_sets.json'
THEMES_FILEPATH = '../backend/static/json/lego_themes.json'


def extract(fp:str):
	return json.load(open(fp, 'r', encoding="utf-8"))


def transform(data:list):
	df = pd.DataFrame(data).reset_index() 
	df.rename(columns={'index': 'id'}, inplace=True)
	df['id'] = df['id'].apply(lambda x: x + 1)

	return df


def load(df:pd.DataFrame, output_fp:str):
	df.to_json(output_fp, indent=4)


if __name__ == '__main__':
	load(
		transform(
			extract(THEMES_FILEPATH)
		),
		output_fp='../backend/static/json/lego_themes_modified.json'
	)