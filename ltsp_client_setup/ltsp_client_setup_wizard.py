from ltsp_client import LtspClient
import ipaddress
import os

class LtspClientSetupWizard:

    def __init__(self, input_file, first_ipaddress=None, dhcp_subclass=None, dnsmasq_tag=None):
        self.dhcp_subclass = dhcp_subclass
        self.dnsmasq_tag = dnsmasq_tag
        self.first_ipaddress = first_ipaddress
        self.ltsp_clients = self.load_ltsp_clients_data(input_file)

    def run(self):
        print("\nBem-vindo ao Assistente de Configuração de Terminais LTSP!")
        primeiro_terminal = 0
        if not self.ltsp_clients[primeiro_terminal].ip_address:
            if not self.first_ipaddress:
                self.first_ipaddress = str(input("\nInforme o endereço IP do primeiro terminal: "))
            for i in range (len(self.ltsp_clients)):
                self.ltsp_clients[i].ip_address = ipaddress.IPv4Address(self.first_ipaddress) + i
        if not self.dhcp_subclass:
            self.dhcp_subclass = str(input("\nInforme a subclasse DHCP: "))
        if not self.dnsmasq_tag:
            self.dnsmasq_tag = str(input("\nInforme a tag dnsmasq: "))

        self.get_dhcp_hosts_declarations()
        print("\n" + self.dnsmasq_tag + "-dhcp.conf pronto!")
        self.get_ltsp_client_sections()
        print("\n" + self.dnsmasq_tag + "-ltsp.conf pronto!")
        self.get_dnsmasq_tag_mac_associations()
        print("\n" + self.dnsmasq_tag + "-dnsmasq.conf pronto!")

    def get_dhcp_hosts_declarations(self):
        try:
            output_file = self.dnsmasq_tag + "-dhcp.conf"
            os.remove(output_file)
        except OSError:
            pass
        with open(output_file, "a") as output_file_append_mode:
            for ltsp_client in self.ltsp_clients:
                output_file_append_mode.write(
                    ltsp_client.get_dhcp_host_declaration(self.dhcp_subclass))
                output_file_append_mode.write("\n\n")
    
    def get_ltsp_client_sections(self):
        try:
            output_file = self.dnsmasq_tag + "-ltsp.conf"
            os.remove(output_file)
        except OSError:
            pass
        with open(output_file, "a") as output_file_append_mode:
            for ltsp_client in self.ltsp_clients:
                output_file_append_mode.write(ltsp_client.get_ltsp_client_section())
                output_file_append_mode.write("\n\n")
    
    def get_dnsmasq_tag_mac_associations(self):
        try:
            output_file = self.dnsmasq_tag + "-dnsmasq.conf"
            os.remove(output_file)
        except OSError:
            pass
        with open(output_file, "a") as output_file_append_mode:
            for ltsp_client in self.ltsp_clients:
                output_file_append_mode.write(ltsp_client.get_dnsmasq_tag_mac_association(self.dnsmasq_tag))

    def load_ltsp_clients_data(self, input_file):
        ltsp_clients = []
        mac_address = 0
        hostname = 1
        password = 3
        ip_address = 4

        with open(input_file, "r") as input_file_read_mode:
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
    try:
        if len(sys.argv) == 2:
            wizard = LtspClientSetupWizard(sys.argv[1])
        elif len(sys.argv) == 3:
            wizard = LtspClientSetupWizard(sys.argv[1], sys.argv[2])
        elif len(sys.argv) == 4:
            wizard = LtspClientSetupWizard(sys.argv[1], sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 5:
            wizard = LtspClientSetupWizard(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        wizard.run()
    except:
        print("""\nFALHA: Arquivo não localizado ou não informado!\n
* É necessário passar o nome do arquivo que contém os dados dos terminais LTSP
  como argumento de linha de comando para o script "ltsp_client_setup_wizard.py".\n""")
