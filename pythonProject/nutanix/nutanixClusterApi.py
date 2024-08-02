import http.client
def listAllNutanix():
    conn = http.client.HTTPSConnection("ssp-china-ntx.ikea.com:9440")

    headers = {
        "Accept": "application/json",
        "Authorization": "Basic <basic_auth_token>",
        "Content-Type": "application/json",
        "Force-Refresh": "string"
    }

    payload = """{
        "kind": "cluster",
        "length": 1,
        "offset": 0,
        "sort_attribute": "string",
        "sort_order": "string"
    }"""

    conn.request("POST", "/api/nutanix/v3/clusters/list", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))