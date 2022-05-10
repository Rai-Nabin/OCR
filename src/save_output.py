import json


def save_to_json(data, FILE_NAME):
    
    with open(f'output/{FILE_NAME}.json', 'wb') as fp:
        fp.write(json.dumps(data, ensure_ascii=False).encode("utf8"))
    print("Saved to JSON...")