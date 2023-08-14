import json
import shutil
from pathlib import Path


def main():
    print('this is step 2')
    with open('./output.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    # print(d)
    Path('./resources/').mkdir(exist_ok=True)
    for key in d:
        item = d[key]
        name = item['name']
        ls = item['imgs']
        shape = len(ls)
        half = int(shape / 2)
        for i in range(shape):
            idx = int(i % half)
            if i < half:
                newName = f'{key}_{name}_{idx}'
            else:
                newName = f'{key}_{name}_{idx}_shiny'
            path = Path(ls[i])
            # print(path.parent / f"{newName}{path.suffix}")
            newName = f"./resources/{newName}{path.suffix}"
            shutil.copyfile(ls[i], newName)
            ls[i] = newName
        item['imgs'] = ls
        d[key] = item

    with open('./data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False))


if __name__ == '__main__':
    main()
