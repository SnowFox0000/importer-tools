import json 

product_cost = 24.8
company_tax_rate = 0.28
GST = 0.15

convertion_rate_USD_NZD = 1.75 #USD-NZD
profit_rate = 0.5

shipping_cost_per_kg = 1.69 # per kg

product_width = 135 # cm
product_height = 19
product_length = 72

nf = 8

product_volume = round(product_width*product_height*product_length, nf)
product_weight = round(product_volume/6000, nf)

shipping_cost = round(product_weight*shipping_cost_per_kg, nf)

profit = round(product_cost*(profit_rate), nf)
company_tax = round(profit*company_tax_rate, nf)
gst = round((product_cost+profit+company_tax+shipping_cost) * 0.15, nf)

product_price = round(product_cost+profit+company_tax+shipping_cost+gst, nf)
product_price_exc_profit_and_tax = round(product_cost+shipping_cost, nf) 

markup_rate = round(product_price/product_cost, nf)
markup_rate_without_shipping_cost = round((product_cost+profit+company_tax+gst)/product_cost, nf)

data = {
		"product volume": product_volume,
		"product weight": product_weight,

		"shipping cost" : shipping_cost,
		"product cost" : product_cost, 
		"product cost nzd": round(product_cost*convertion_rate_USD_NZD, 2),

		"profit" : profit,
		"company tax" : company_tax,
		"gst" : gst,

		"product price": product_price,
		"product price nzd": round(product_price*convertion_rate_USD_NZD, 2),

		"product price exc profit and tax nzd": round(product_price_exc_profit_and_tax*convertion_rate_USD_NZD, 2),
		"markup rate": markup_rate,
		# "markup rate without shipping cost": markup_rate_without_shipping_cost,
		}

print(json.dumps(data, indent=4))