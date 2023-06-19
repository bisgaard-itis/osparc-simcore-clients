from argparse import ArgumentParser
from pathlib import Path
import json
from typing import List

def main(data: json.JSONDecoder, entries: List[str]):
    try:
        for elm in entries:
            if isinstance(data, list):
                data = data[int(elm)]
            else:
                data = data.get(elm)
    except Exception as e:
        print(f"Could not get elm={elm} from data={data}")
        raise e
    print(data)

if __name__ == '__main__':
    parser = ArgumentParser('Get entries from a json file/string')
    parser.add_argument('entry', help='entry in json, separated by ".". E.g. "info.title"', type=str)
    parser.add_argument('json', help='json string/file', type=str)

    args = parser.parse_args()
    if Path(args.json).is_file():
        with open(args.json,'r') as f:
            data = json.load(f)
    else:
        data = json.loads(args.json)

    main(data, args.entry.split("."))
