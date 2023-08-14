import json
from html.parser import HTMLParser
from pathlib import Path


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.d = {}

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    # print(f"     attr: {attr[1]}")
                    self.d[self.count]['imgs'].append(attr[1])

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        data = data.replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        size = len(data)
        if size > 0:
            if '~' not in data:
                self.count += 1
                self.d[self.count] = {
                    'id': self.count,
                    'name': data,
                    'imgs': []
                }
            #     print(f'{self.count}: "{data}"')
            # else:
            #     print(f'"{data}"')


def main():
    print('this is step 1')
    with open('datasrc.html', encoding='utf-8') as f:
        text = f.read()
    parser = MyHTMLParser()
    parser.feed(text)

    with open('./output.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(parser.d, ensure_ascii=False))
    Path('./resources').mkdir(exist_ok=True)


if __name__ == '__main__':
    main()
