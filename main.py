import xml.dom.minidom

# C:\\Users\\felli\\Downloads\\dam_reports\\

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
    itemlist = xmldoc.getElementsByTagName('port')  # pega os itens da tag port do documento xml e joga na lista
    opened = []
    final = []
    for item in itemlist:
        if item.childNodes[0].attributes['state'].value == 'open' or item.childNodes[0].attributes[
            'state'].value == 'closed':
            opened.append(item.attributes['portid'].value)
            final = list(map(int, opened))  # converte para valores inteiros
            final.sort()
    return final


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
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)
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
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)

        if result_wan_dmz == []:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Your network (wan->dmz) was correctly configured")
        else:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("wan->dmz: ", result_wan_dmz)
        if result_dmz_wan == []:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Your network (dmz->wan) was correctly configured")
        else:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            print("dmz->wan: ", result_dmz_wan)

        if result_dmz_lan == []:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Your network (dmz->lan) was correctly configured")
        else:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("dmz->lan: ", result_dmz_lan)
        if result_lan_dmz == []:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Your network (lan->dmz) was correctly configured")
        else:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->dmz: ", result_lan_dmz)
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
        else:
            print("------------------")
            print("LAN -> WAN status:")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->wan: ", result_lan_wan)
        if result_wan_lan == []:
            print("------------------")
            print("WAN -> LAN status:")
            print("Your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("WAN -> LAN status:")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("wan->lan: ", result_wan_lan)

        if result_wan_dmz == []:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Your network (wan->dmz) was correctly configured")
        else:
            print("------------------")
            print("WAN -> DMZ status:")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("wan->dmz: ", result_wan_dmz)
        if result_dmz_wan == []:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Your network (dmz->wan) was correctly configured")
        else:
            print("------------------")
            print("DMZ -> WAN status:")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            print("dmz->wan: ", result_dmz_wan)

        if result_dmz_lan == []:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Your network (dmz->lan) was correctly configured")
        else:
            print("------------------")
            print("DMZ -> LAN status:")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            print("dmz->lan: ", result_dmz_lan)
        if result_lan_dmz == []:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Your network (lan->dmz) was correctly configured")
        else:
            print("------------------")
            print("LAN -> DMZ status:")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            print("lan->dmz: ", result_lan_dmz)

    else:
        print("ERROR, select one valid option")
