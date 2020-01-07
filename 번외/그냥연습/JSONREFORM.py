import json


def django_fixture_reformer(input_json_name, output_json_name, model_name):
    items = []

    with open(f"{input_json_name}.json") as json_file:
        json_data = json.load(json_file)

        for data in json_data:
            reformat_data = {
                "model": model_name,
                "pk": data['id'],
                "fields": {
                    **data
                }
            }

            del reformat_data["fields"]["id"]

            items.append(reformat_data)

    with open(f"{output_json_name}.json", 'w') as json_file:
        json.dump(items, json_file)


django_fixture_reformer('item-data-test', 'item-data-reform', 'item.item')
