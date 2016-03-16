import json


def write_json(client):
    """example = {
        "M1": [
            {
                "Ip": "10.10.194.2",
                "Netmask": "255.255.0.0"
            }
        ],
        "MF1": [
            {
                "Ip": "192.168.1.48",
                "Netmask": "255.255.255.0"
            }
        ]
    }
    """
    append_data = {
            client[0]: [
                {
                    "Ip": client[1],
                    "Netmask": client[2]
                }
            ]
        }

    with open('data.json') as outdata:
        try:
            data = json.load(outdata)
            data.update(append_data)
        except(ValueError, TypeError, NameError):
            data = append_data

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def read_json():

    with open('data.json') as json_data:
        data = json.load(json_data)
        json_data.close()
        clients_list = []
        for item in data:
            parameters = data[item]
            ip = parameters[0]['Ip']
            netmask = parameters[0]['Netmask']
            clients_list.append([item, ip, netmask])
    return clients_list
