import wmi


def ipstaticchanger(ip, subnet):
    nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    nic = nic_config[0]

    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnet])

    return nic


def ipdhcp():
    nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    nic = nic_config[0]

    nic.EnableDHCP()

    return nic
