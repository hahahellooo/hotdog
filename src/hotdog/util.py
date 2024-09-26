def get_max_score(p):
    max_score = 0
    max_label = ''
    for item in p:
        if item['score'] > max_score:
            max_score = round(item['score'],4)
            max_label = item['label']
            message = f'{max_score}확률로 {max_label}입니다.'
        return message
