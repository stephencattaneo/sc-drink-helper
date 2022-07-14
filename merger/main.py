import codecs
import json
import sys


class Merger:
    input = None
    data = None

    def __init__(self, input, datapath) -> None:
        self.datapath = datapath

        with open(input) as fd:
            self.input = json.load(fd)

        with open(datapath) as fd:
            self.data = json.load(fd)

    def run(self):
        found = False
        i = 0
        length = len(self.data)

        while not found and i < length:
            if self.data[i]['name'] == self.input['name']:
                self.data[i]['ingredients'] = self.input['ingredients']
                found = True
            else:
                i += 1

        if not found:
            raise Exception(f'could not find {self.input["name"]}')


    def write(self):
        with codecs.open(self.datapath, 'w', encoding='utf-8') as fd:
            json.dump(self.data, fd, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    input = sys.argv[1]
    datapath = sys.argv[2]
    print(f'addding {input} to {datapath}')

    merge = Merger(input=input, datapath=datapath)
    merge.run()

    print(f'writing to {datapath}')
    merge.write()

