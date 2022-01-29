

class DeprecatedModules():
    def __init__(self, name = "DeprecatedModules", criticity = "HIGHEST", grade=0, maxgrade=0, comment=""):
        self.grade = grade
        self.maxgrade = maxgrade
        self.name = name
        self.criticity = criticity
        self.comment = comment

    def evaluate(self):
        print("Evaluating Good Practice " + self.__class__.__name__)
        print("Found use of  " + str(self.grade) + " deprecated modules")
        

    def parse(self, filelist):

        modules = [
            "accelerate",
            "aos_asn_pool",
            "aos_blueprint",
            "aos_blueprint_param",
            "aos_blueprint_virtnet",
            "aos_device",
            "aos_external_router",
            "aos_ip_pool",
            "aos_logical_device",
            "aos_logical_device_map",
            "aos_login",
            "aos_rack_type",
            "aos_template",
            "azure",
            "cl_bond",
            "cl_bridge",
            "cl_img_install",
            "cl_interface",
            "cl_interface_policy",
            "cl_license",
            "cl_ports",
            "cs_nic",
            "docker",
            "ec2_ami_find",
            "ec2_ami_search",
            "ec2_remote_facts",
            "ec2_vpc",
            "kubernetes",
            "netscaler",
            "nxos_ip_interface",
            "nxos_mtu",
            "nxos_portchannel",
            "nxos_switchport",
            "oc",
            "panos_nat_policy",
            "panos_security_policy",
            "vsphere_guest",
            "win_msi",
            "include",
        ]
        for file in filelist:
            length = len(filelist)
        print("Evaluating " + str(length) + " files...")
        counter = 0
        badGradeCounter = 0
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            for line in f:
                for i in modules:
                    if i+":" in line:
                        print(
                            "Detected usage of deprecated module "
                            + i
                            + " in file "
                            + file
                        )
                        badGradeCounter += 1
            counter += 1

        self.maxgrade = counter
        self.grade = badGradeCounter
