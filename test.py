def count(comment):
    res = comment % 10
    if comment == 0:
        return 'Нет комментариев'
    elif res == 1:
        return f'{comment} Комментарий'
    elif comment > 4 and comment < 21:
        return f'{comment} Комментариев'
    elif res > 1 and res < 5:
        return f'{comment} Комментария'
    return f'{comment} Комментариев'


for i in range(51):
    print(count(i))
