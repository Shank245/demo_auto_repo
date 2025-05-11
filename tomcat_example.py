import os


class Tomcat:

    def get_details_for_each_tomat(self, server_xml):
        self.tcf = server_xml
        self.th = os.path.dirname(server_xml)
        return None

    def display_details(self):
        print("Tomcat Configuration File: ", self.tcf)
        print("Tomcat Home Directory: ", self.th)
        return None


def main():
    tomcat7 = Tomcat()
    tomcat9 = Tomcat()

    # Initialize details for each Tomcat instance
    tomcat7.get_details_for_each_tomat("/opt/tomcat7/conf/server.xml")
    tomcat9.get_details_for_each_tomat("/opt/tomcat9/conf/server.xml")
    tomcat7.display_details()
    tomcat9.display_details()
    return None


if __name__ == "__main__":
    main()
    # tomcat7.get_details_for_each_tomat("/opt/tomcat7/conf/server.xml")
    # tomcat9.get_details_for_each_tomat("/opt/tomcat9/conf/server.xml")
    # tomcat7.display_details()
    # tomcat9.display_details()
