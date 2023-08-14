import json
# from pathlib import Path


def main():
    print('this is step 3')
    with open('data.json', 'r', encoding='utf-8') as f:
        d = json.load(f)

    with open('pokemonsv.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    first = True
    for line in lines:
        if first:
            first = False
            continue
        each = line.replace('\t\t', '\t').replace('\r', '').replace('\n', '').split('\t')
        iid = int(each[0].replace('#', ''))
        fid = int(each[1].replace('#', ''))
        item = d[str(iid)]
        item['fid'] = fid
        item['types'] = each[3:]
        d[str(iid)] = item

    with open('resources/data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False))


if __name__ == '__main__':
    main()
