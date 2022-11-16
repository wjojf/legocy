from themes_etl import extract
import json 


THEMES_MODIFIED_FILEPATH  = '../backend/static/json/lego_themes_modified.json'
OUTPUT_FP = '../backend/static/json/lego_thems_final.json'


def transform(_dict):
	output = []

	if "id" not in _dict or "name" not in _dict:
		return []

	ids = list(_dict["id"].keys())

	for id_ in ids:
		try:
			theme_name = _dict["name"][id_]
		except KeyError:
			print(f'Could not find theme with id={id_}')
			continue
		output.append({
				"id": int(id_) + 1,
				"name": theme_name
			})

	return output


def load(_list, output_fp):
	json.dump(_list, output_fp, indent=4)


if __name__ == '__main__':
	load(
		transform(
			extract(
				THEMES_MODIFIED_FILEPATH
			)
		),
		output_fp=open(OUTPUT_FP, 'w')
	)