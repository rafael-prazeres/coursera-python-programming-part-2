from ltsp_client import LtspClient
import ipaddress

class LtspClientSetupWizard:

    def __init__(self, input_file, network_cidr=None, dhcp_subclass=None, dnsmasq_tag=None):
        self.dhcp_subclass = dhcp_subclass
        self.dnsmasq_tag = dnsmasq_tag
        self.network_cidr = network_cidr
        self.ltsp_clients = self.load_ltsp_clients(input_file)

    def run(self):
        if not self.network_cidr:
            self.network_cidr = str(input("Informe o CIDR: "))
        if not self.dhcp_subclass:
            self.dhcp_subclass = str(input("Informe a subclasse DHCP: "))
        if not self.dnsmasq_tag:
            self.dnsmasq_tag = str(input("Informe a tag dnsmasq: "))
        for ltsp_client in self.ltsp_clients:
            # print (ltsp_client)
            # print (ltsp_client.get_dhcp_host_declaration(self.dhcp_subclass))
            print("")

    def load_ltsp_clients(self, input_file):
        ltsp_clients = []
        mac_address = 0
        hostname = 1
        password = 3
        ip_address = 4

        input_file_read_mode = open(input_file, "r")

        for line in input_file_read_mode:
            client_data = line.split()
            if len(client_data) == 2:
                ltsp_client = LtspClient(
                    client_data[mac_address],
                    client_data[hostname])
            elif en(ltsp_client_data) == 3:
                ltsp_client = LtspClient(
                    client_data[mac_address],
                    client_data[hostname],
                    client[password])
            elif en(ltsp_client_data) == 4:
                ltsp_client = LtspClient(
                    client_data[mac_address],
                    client_data[hostname],
                    client[password],
                    client_data[ip_address])
            else:
                ltsp_client = LtspClient()
            ltsp_clients.append(ltsp_client)

        return ltsp_clients


if __name__ == "__main__":
    import sys
    wizard = LtspClientSetupWizard(sys.argv[1])
    wizard.run()
