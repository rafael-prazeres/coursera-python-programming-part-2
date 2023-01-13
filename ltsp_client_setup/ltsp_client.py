import base64

class LtspClient:
    '''
        A classe LtspClient modela um cliente LTSP a ser utilizado
        no processo de configuração/autorização em lote de clientes LTSP.
    '''

    def __init__(self, mac_address=None, hostname=None, password="labinfo", ip_address=None):
        self.mac_address = mac_address
        self.hostname = hostname
        self.ip_address = ip_address
        self.password = base64.b64encode((password+"\n").encode())

    def __str__(self):
        if self.ip_address is not None:
            return "{0} {1} {2} {3}".format(
                self.mac_address,
                self.hostname,
                self.password.decode(),
                self.ip_address)
                
        else:
            return "{0} {1} {2}".format(
                self.mac_address,
                self.hostname,
                self.password.decode())

    def get_dhcp_host_declaration(self, subclass):
        if self.ip_address is not None:
            return '''host %s {
    hardware ethernet %s;
    fixed-address %s;
}
subclass "%s" 1:%s;'''%(
                self.hostname,
                self.mac_address,
                self.ip_address,
                subclass,
                self.mac_address)
        else:
            return '''host %s {
    hardware ethernet %s;
}
subclass "%s" 1:%s;'''%(
                self.hostname,
                self.mac_address,
                subclass,
                self.mac_address)            

    def get_ltsp_client_section(self):
        return '''[{0}]
HOSTNAME={1}
AUTOLOGIN={1}
PASSWORDS_{1}="{1}/{2}"'''.format(
            self.mac_address,
            self.hostname,
            self.password.decode()
    )

    def get_dnsmasq_tag_mac_association(self, tag):
        return "dhcp-mac=set:{0},{1}".format(tag, self.mac_address)
