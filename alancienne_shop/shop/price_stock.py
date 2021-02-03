def price_ttc(prix, tva):
    price_ttc = prix*(1+(tva/100))
    return price_ttc


def available_stock(max_stock, quantity):
    stock_available = max_stock - quantity
    return stock_available
