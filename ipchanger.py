import wmi
import nmap
import time

class IpChanger:
    """
    Ip Changer class is based on WMI protocol. Used to read local network cards to list and manage their settings.
    """
    def __init__(self):
        self.nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    def ip_static_changer(self, device, ip, subnet):
        """
        Change Ip to static address
        :param device: int number of device on WMI list - parameter is generated in 'get_network_device_list()'
        :param ip: string of Ip address what we would to change
        :param subnet: string of Subnet address what we would to change
        :return: int result of operation
        """
        result = self.nic_config[device].EnableStatic(IPAddress=[ip], SubnetMask=[subnet])

        return result[0]

    def ip_dhcp(self, device):
        """
        Change Ip to DHCP mode
        :param device: int number of device on WMI list - parameter is generated in 'get_network_device_list()'
        :return: int result of operation
        """
        result = self.nic_config[device].EnableDHCP()

        return result[0]

    def get_network_device_list(self):
        """
        Reading WMI protocol to get network cards list
        :return: list of active network devices on local computer [number of device, human readable name of network card]
        """
        active_network_device_number = len(self.nic_config)
        active_network_device_list = []
        for i in range(0, active_network_device_number):
            active_network_device_list.append([str(i), self.nic_config[i].Description])
        return active_network_device_list

    def find_free_ip_address(self, ip_family):
        ip_family += "/24"
        nm = nmap.PortScanner()
        nm.scan(hosts=ip_family, arguments='-v -sn -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        hosts_list.sort()
        for host, status in reversed(hosts_list):
            if status == "down" or status == "up":
                print('{0}:{1}'.format(host, status))
                return host

