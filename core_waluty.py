import json
import urllib.request
import urllib.error

class CurrencyConverter:
    def getValue(symbol):
	    req = "http://api.nbp.pl/api/exchangerates/rates/A/" + symbol
	    try:
	        with urllib.request.urlopen(req) as nbp:
	            result = nbp.read().decode('utf-8')
	    except urllib.error.HTTPError:
	        return None
	    value = json.JSONDecoder().decode(result)
	    return value["rates"][0]["mid"]
