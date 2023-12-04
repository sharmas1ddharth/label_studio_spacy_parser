spacy_data = []
for i in data:
    text = i['data']['text']
    annotations = {}
    for annot in i['annotations']:
        entities_list = []
        for result in annot['result']:
            if 'value' in result.keys():
                start = result['value']['start']
                end = result['value']['end']
                label = result['value']['labels'][0]
                entities = (start, end, label)
                entities_list.append(entities)
        annotations['entities'] = entities_list
    spacy_data.append((text, annotations))
