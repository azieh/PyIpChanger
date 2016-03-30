import json
import os
import stat
"""
Example to init some JSON list
example = {
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


def write_json(client):
    """
    Write JSON file a network card parameter for each line
    :param client: list of client parameter [name of line, ip, subnet]
    :return: null
    """
    append_data = {
            client[0]:
            [
                {
                    "Ip": client[1],
                    "Subnet": client[2]
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

    """
    Read JSON file
    :return:
    """
    clients_list = []
    try:
        with open('data.json', 'r') as json_data:
            try:
                data = json.load(json_data)
                json_data.close()
            except ValueError:
                print("Json file is empty or something goes wrong")
                clients_list.append(['Null', 'Null', 'Null'])
                return clients_list

            for item in data:
                parameters = data[item]
                ip = parameters[0]['Ip']
                subnet = parameters[0]['Subnet']
                clients_list.append([item, ip, subnet])
    except EnvironmentError:
        print("There is no JSON file")
        with open('data.json', 'w+') as json_data:
            print("Json file was created: " + str(json_data))
            read_json()

    return clients_list


def delete_data(client):

    with open('data.json', 'r') as json_data:
        try:
            data = json.load(json_data)
            json_data.close()
        except ValueError:
                print("Json file is empty or something goes wrong")
        try:
            del data[client[0]]
        except KeyError:
            pass
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
