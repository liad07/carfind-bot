import urllib.request, json

def sample_res(x):
    url = 'https://data.gov.il/api/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&filters={"mispar_rechev":"' + x + '"}'

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    x = str(data)
    x = x.replace("{", "")
    x = x.replace("}", "")
    x = x.replace("]", "")
    x = x.replace("[", "")
    x = x.replace("'", "")
    x = x.replace("result:", "")
    x = x.split(",")
    y = x[9:32]
    d = ""
    for i in range(len(y)):
        d += y[i] + "\n"
    return d