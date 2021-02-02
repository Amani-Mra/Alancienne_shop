def price_ttc(prix, tva):
    price_ttc = prix*(1+(tva/100))
    return price_ttc
