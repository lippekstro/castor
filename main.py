import xml.dom.minidom
import datetime
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Castor Network Report', 1, 0, 'C')
        # Line break
        self.ln(20)


class PDF(FPDF):
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Print centered page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

        ct = datetime.datetime.now()
        d = ct.strftime("%m/%d/%Y, %H:%M:%S")
        pdf.set_x(150)
        pdf.cell(0, 10, d, 0, 0, 'R')

prompt = ">"
checker = True

# lan->wan
lan_wan_no_dmz = [21, 22, 23, 80, 110, 143, 443, 993, 995]
wan_lan_no_dmz = [22, 23, 25, 80, 143, 443, 993]

# dmz
dmz_lan_wan = [21, 22, 23, 80, 110, 143, 443, 993, 995]
dmz_wan_lan = [22, 23, 25, 80, 143, 443, 993]
dmz_wan_dmz = [21, 53, 80, 110, 443, 995]
dmz_dmz_wan = [53, 80, 443]
dmz_dmz_lan = [25, 53, 80, 110, 143, 443, 993, 995]
dmz_lan_dmz = [21, 53, 80, 143, 443, 993]

# app corp
app_dmz_lan = [25, 53, 80, 110, 143, 443, 993, 995, 1433]
app_lan_dmz = [21, 53, 80, 143, 443, 993, 1433]


def xml_reading(analysis):
    xmldoc = xml.dom.minidom.parse(analysis)
    itemlist = xmldoc.getElementsByTagName('port')
    opened = []
    final = []
    for item in itemlist:
        if item.childNodes[0].attributes['state'].value == 'open' \
                or item.childNodes[0].attributes['state'].value == 'closed':
            opened.append(item.attributes['portid'].value)
            final = list(map(int, opened))
            final.sort()
    return final


pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_auto_page_break(True)
pdf.set_xy(0.0, 0.0)
pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(0, 0, 255)
pdf.cell(w=210.0, h=40.0, align='C', txt="CASTOR NETWORK REPORT", border=0)
pdf.set_font('Arial', '', 12)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(10, 30)

while checker:
    print("Which model you want check? ")
    print("1 - Infrastructure without DMZ")
    print("2 - Infrastructure with DMZ")
    print("3 - Infrastructure with DMZ and Corporate Application")
    model = input(prompt)

    if model == "1":
        checker = False
        print("Enter LAN->WAN analysis path: ")
        reading = input(prompt)
        lan_wan_analysis = xml_reading(reading)

        print("Enter WAN->LAN analysis path: ")
        reading = input(prompt)
        wan_lan_analysis = xml_reading(reading)

        print(f"The model without DMZ (lan->wan) is: ", lan_wan_no_dmz)
        print(f"The report of your network: ", lan_wan_analysis)
        print(f"The model without DMZ (wan->lan) is: ", wan_lan_no_dmz)
        print(f"The report of your network: ", wan_lan_analysis)

        result_lan_wan = list(set(lan_wan_analysis) - set(lan_wan_no_dmz))
        result_lan_wan.sort()

        result_wan_lan = list(set(wan_lan_analysis) - set(wan_lan_no_dmz))
        result_wan_lan.sort()

        if result_lan_wan == []:
            print("------------------")
            print("LAN -> WAN status:")
            print("Your network (lan->wan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (lan=>wan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Lan=>Wan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_lan_wan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (wan=>lan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Wan=>Lan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): High')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_wan_lan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
    elif model == "2":
        checker = False
        print("Enter LAN->WAN analysis path: ")
        reading = input(prompt)
        lan_wan_analysis = xml_reading(reading)

        print("Enter WAN->LAN analysis path: ")
        reading = input(prompt)
        wan_lan_analysis = xml_reading(reading)

        print("Enter WAN->DMZ analysis path: ")
        reading = input(prompt)
        wan_dmz_analysis = xml_reading(reading)

        print("Enter DMZ->WAN analysis path: ")
        reading = input(prompt)
        dmz_wan_analysis = xml_reading(reading)

        print("Enter DMZ->LAN analysis path: ")
        reading = input(prompt)
        dmz_lan_analysis = xml_reading(reading)

        print("Enter LAN->DMZ analysis path: ")
        reading = input(prompt)
        lan_dmz_analysis = xml_reading(reading)

        print(f"The model with DMZ (lan->wan) is: ", dmz_lan_wan)
        print(f"The report of your network: ", lan_wan_analysis)
        print(f"The model with DMZ (wan->lan) is: ", dmz_wan_lan)
        print(f"The report of your network: ", wan_lan_analysis)

        print(f"The model with DMZ (wan->dmz) is: ", dmz_wan_dmz)
        print(f"The report of your network: ", wan_dmz_analysis)
        print(f"The model with DMZ (dmz->wan) is: ", dmz_dmz_wan)
        print(f"The report of your network: ", dmz_wan_analysis)

        print(f"The model with DMZ (dmz->lan) is: ", dmz_dmz_lan)
        print(f"The report of your network: ", dmz_lan_analysis)
        print(f"The model with DMZ (lan->dmz) is: ", dmz_lan_dmz)
        print(f"The report of your network: ", lan_dmz_analysis)

        result_lan_wan = list(set(lan_wan_analysis) - set(lan_wan_no_dmz))
        result_lan_wan.sort()

        result_wan_lan = list(set(wan_lan_analysis) - set(wan_lan_no_dmz))
        result_wan_lan.sort()

        result_wan_dmz = list(set(wan_dmz_analysis) - set(dmz_wan_dmz))
        result_wan_dmz.sort()

        result_dmz_wan = list(set(dmz_wan_analysis) - set(dmz_dmz_wan))
        result_dmz_wan.sort()

        result_dmz_lan = list(set(dmz_lan_analysis) - set(dmz_dmz_lan))
        result_dmz_lan.sort()

        result_lan_dmz = list(set(lan_dmz_analysis) - set(dmz_lan_dmz))
        result_lan_dmz.sort()

        if result_lan_wan == []:
            print("------------------")
            print("LAN -> WAN status:")
            print("Your network (lan->wan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (lan=>wan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Lan=>Wan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_lan_wan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (wan=>lan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Wan=>Lan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): High')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_wan_lan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_wan_dmz == []:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Your network (wan->dmz) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (wan=>dmz) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("wan->dmz: ", result_wan_dmz)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Wan=>Dmz analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_wan_dmz))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_dmz_wan == []:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Your network (dmz->wan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (dmz=>wan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            print("dmz->wan: ", result_dmz_wan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Dmz=>Wan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Low')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_dmz_wan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_dmz_lan == []:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Your network (dmz->lan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (dmz=>lan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("dmz->lan: ", result_dmz_lan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Dmz=>Lan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): High')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_dmz_lan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_lan_dmz == []:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Your network (lan->dmz) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (lan=>dmz) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->dmz: ", result_lan_dmz)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Lan=>Dmz analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_lan_dmz))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
    elif model == "3":
        checker = False
        print("Enter your Corporate Application port number: ")
        corp_app_port = int(input(prompt))
        # print("Enter your Database port number: ")
        db_port = 1433

        print("Enter LAN->WAN analysis path: ")
        reading = input(prompt)
        lan_wan_analysis = xml_reading(reading)

        print("Enter WAN->LAN analysis path: ")
        reading = input(prompt)
        wan_lan_analysis = xml_reading(reading)

        print("Enter WAN->DMZ analysis path: ")
        reading = input(prompt)
        wan_dmz_analysis = xml_reading(reading)
        dmz_wan_dmz.append(corp_app_port)
        dmz_wan_dmz.sort()

        print("Enter DMZ->WAN analysis path: ")
        reading = input(prompt)
        dmz_wan_analysis = xml_reading(reading)
        dmz_dmz_wan.append(corp_app_port)
        dmz_dmz_wan.sort()

        print("Enter DMZ->LAN analysis path: ")
        reading = input(prompt)
        dmz_lan_analysis = xml_reading(reading)
        dmz_dmz_lan.append(corp_app_port)
        dmz_dmz_lan.append(db_port)
        dmz_dmz_lan.sort()

        print("Enter LAN->DMZ analysis path: ")
        reading = input(prompt)
        lan_dmz_analysis = xml_reading(reading)
        dmz_lan_dmz.append(corp_app_port)
        dmz_lan_dmz.append(db_port)
        dmz_lan_dmz.sort()

        print(f"The model with DMZ and Application (lan->wan) is: ", dmz_lan_wan)
        print(f"The report of your network: ", lan_wan_analysis)
        print(f"The model with DMZ and Application (wan->lan) is: ", dmz_wan_lan)
        print(f"The report of your network: ", wan_lan_analysis)

        print(f"The model with DMZ and Application (wan->dmz) is: ", dmz_wan_dmz)
        print(f"The report of your network: ", wan_dmz_analysis)
        print(f"The model with DMZ and Application (dmz->wan) is: ", dmz_dmz_wan)
        print(f"The report of your network: ", dmz_wan_analysis)

        print(f"The model with DMZ and Application (dmz->lan) is: ", app_dmz_lan)
        print(f"The report of your network: ", dmz_lan_analysis)
        print(f"The model with DMZ and Application (lan->dmz) is: ", app_lan_dmz)
        print(f"The report of your network: ", lan_dmz_analysis)

        result_lan_wan = list(set(lan_wan_analysis) - set(lan_wan_no_dmz))
        result_lan_wan.sort()

        result_wan_lan = list(set(wan_lan_analysis) - set(wan_lan_no_dmz))
        result_wan_lan.sort()

        result_wan_dmz = list(set(wan_dmz_analysis) - set(dmz_wan_dmz))
        result_wan_dmz.sort()

        result_dmz_wan = list(set(dmz_wan_analysis) - set(dmz_dmz_wan))
        result_dmz_wan.sort()

        result_dmz_lan = list(set(dmz_lan_analysis) - set(dmz_dmz_lan))
        result_dmz_lan.sort()

        result_lan_dmz = list(set(lan_dmz_analysis) - set(dmz_lan_dmz))
        result_lan_dmz.sort()

        if result_lan_wan == []:
            print("------------------")
            print("LAN -> WAN status:")
            print("Your network (lan->wan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (lan=>wan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Lan=>Wan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_lan_wan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (wan=>lan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Wan=>Lan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): High')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_wan_lan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)

        if result_wan_dmz == []:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Your network (wan->dmz) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (wan=>dmz) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("wan->dmz: ", result_wan_dmz)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='WAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Wan=>Dmz analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_wan_dmz))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_dmz_wan == []:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Your network (dmz->wan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (dmz=>wan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            print("dmz->wan: ", result_dmz_wan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => WAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Dmz=>Wan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Low')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_dmz_wan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)

        if result_dmz_lan == []:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Your network (dmz->lan) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (dmz=>lan) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("dmz->lan: ", result_dmz_lan)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='DMZ => LAN status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Dmz=>Lan analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): High')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_dmz_lan))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)
        if result_lan_dmz == []:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Your network (lan->dmz) was correctly configured")

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Your network (lan=>dmz) was correctly configured')
            pdf.ln(5)
        else:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->dmz: ", result_lan_dmz)

            pdf.cell(0, 0, txt='------------------')
            pdf.ln(5)
            pdf.cell(0, 0, txt='LAN => DMZ status:')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Lan=>Dmz analysis and recommended model are different')
            pdf.ln(5)
            pdf.cell(0, 0, txt='Vulnerability Level (DAM): Medium')
            pdf.ln(5)
            pdf.cell(0, 0, txt='we recommend that you close the following ports: ')
            pdf.ln(5)
            mystr = ', '.join(map(str, result_lan_dmz))
            pdf.cell(0, 0, mystr)
            pdf.ln(5)

    else:
        print("ERROR, select one valid option")

pdf.output('Castor_Report.pdf')
print("------------------")
print("Relatório Gerado")
