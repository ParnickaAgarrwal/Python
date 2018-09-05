#WEB API'S USING PYTHON
import requests
import json
response=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=159029")
quote=json.loads(response.text)
print(quote["quoteText"])
