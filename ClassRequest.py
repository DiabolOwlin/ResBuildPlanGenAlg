import requests


class Request:
    token = "secret_T45iO2TZOukJtJQLW5vSf7POJa2W9v7RLQSeLFeMVxb"
    databaseID = 'b2cb393e7412464cb51ad5f5d9360bae'

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    def __init__(self):
        self.params = None
        self.data = None
        self.end_apartments = []
        self.row_apartments = []

    def define_params(self, apart_type):
        self.params = {
            "filter": {
                "property": "Type",
                "multi_select": {
                    "contains": f"{apart_type}"
                }
            }
        }
        return self.params

    def query_database(self, apart_type):
        params = self.define_params(apart_type)
        read_url = f"https://api.notion.com/v1/databases/{self.databaseID}/query"
        res = requests.request("POST", read_url, json=params, headers=self.headers)
        data = res.json()
        self.data = data.get('results')

    def unpack_response(self, apart_list):
        for _ in range(len(self.data)):
            type_name = self.data[_].get('properties').get('Type').get('multi_select')[0].get('name')[0]
            rooms_count = self.data[_].get('properties').get('Rooms').get('multi_select')[0].get('name')
            layout = self.data[_].get('properties').get('Layout').get('files')[0].get('file').get('url')
            width = self.data[_].get('properties').get('Width').get('number')
            depth = self.data[_].get('properties').get('Depth').get('number')

            apart_list.append(
                [{'Type': type_name, 'Rooms': rooms_count}, [layout], {'Width': width, 'Depth': depth}])
