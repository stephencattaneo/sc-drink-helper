import codecs
import json
from io import StringIO
import re
import sys


class Processor:
    filename = None
    input = None
    output = None
    amt_pattern = r'(?P<amount>\w+ ((ounces?)|(dash(es)?)|(teaspoon)))'
    name_pattern = r'(?P<name>\w+( [\w.\']+)*)( \(page (?P<page>\d+)\))?'
    number_pattern = r'(?P<num>\d+)'

    def __init__(self, **kwargs) -> None:
        input = kwargs['input']

        if type(input) == str:
            self.filename = input
            with open(self.filename) as fd:
                self.input = fd.read().splitlines()

        elif type(input) == StringIO:
            self.input = input.read().splitlines()

        self.line_rx = re.compile(f'^({self.amt_pattern} {self.name_pattern})|{self.number_pattern}$')

    def run(self) -> int:
        name = ''
        ingredients = []

        linecount = 0

        for line in self.input:
            if linecount == 0:
                name = line
            else:
                self.processLine(line, ingredients)

            linecount += 1

        self.output = {
            "name": name,
            "ingredients": ingredients,
        }

        return len(ingredients)

    def processLine(self, line, ingredients):
        match = self.line_rx.match(line)
        if match:
            matchdict = match.groupdict()
            if matchdict['num']:
                ingredients[-1]['rum_category'] = matchdict['num']
            else:
                ingredients.append(matchdict)
        else:
            raise Exception(f'Could not match: "{line}"')

    def output(self):
        return self.output

    def write(self, filename):
        with codecs.open(filename, 'w', encoding='utf-8') as fd:
            json.dump(self.output, fd, ensure_ascii=False)


if __name__ == '__main__':
    filename = sys.argv[1]
    print(f'processing to {filename}')
    proc = Processor(input=filename)
    proc.run()
    outname = '.'.join([filename.split('.')[0], 'json'])
    print(f'printing to {outname}')
    proc.write(outname)