import wmi


class IpChanger():

    def __init__(self):
        self.nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    def ip_static_changer(self, device, ip, subnet):

        result = self.nic_config[device].EnableStatic(IPAddress=[ip], SubnetMask=[subnet])

        return result

    def ip_dhcp(self, device):

        result = self.nic_config[device].EnableDHCP()

        return result

    def get_network_device_list(self):
        active_network_device_number = len(self.nic_config)
        active_network_device_list = []
        #print(self.nic_config)
        for i in range(0, active_network_device_number):
            active_network_device_list.append([str(i), self.nic_config[i].Description])
        return active_network_device_list
