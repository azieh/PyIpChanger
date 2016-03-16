import wmi


def ip_static_changer(device, ip, subnet):

    result = device.EnableStatic(IPAddress=[ip], SubnetMask=[subnet])

    return result


def ip_dhcp(device):

    result = device.EnableDHCP()

    return result


def get_network_device_list():
    nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    active_network_device_number = len(nic_config)
    active_network_device_list = []
    for i in range(0, active_network_device_number):
        active_network_device_list.append([str(i), nic_config[i].Description])
        print(nic_config[i])
    print(active_network_device_list)
    return active_network_device_list
