# Help the bookseller ! - 6kyu


def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_art:
        return ''

    category_to_quantity = {}
    for cat in list_of_cat:
        quantity = 0
        for stock in list_of_art:
            if stock.startswith(cat):
                quantity += int(stock.split(' ')[1])
        category_to_quantity[cat] = quantity

    return ' - '.join([f'({x} : {y})' for x, y in category_to_quantity.items()])


print(stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]))
