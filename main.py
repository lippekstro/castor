import xml.dom.minidom

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
    itemList = xmldoc.getElementsByTagName('port')  # pega os itens da tag port do documento xml e joga na lista
    open = []
    for item in itemList:
        if item.childNodes[0].attributes['state'].value == 'open':  # considera apenas as portas abertas
            open.append(item.attributes['portid'].value)
            final = list(map(int, open))  # converte para valores inteiros
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

        if lan_wan_no_dmz == lan_wan_analysis:
            print("Both are equals, your network (lan->wan) was correctly configured")
        else:
            print("------------------")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            lan_wan_close = list(set(lan_wan_analysis)-set(lan_wan_no_dmz))
            lan_wan_close.sort()
            print("lan->wan: ", lan_wan_close)
        if wan_lan_no_dmz == wan_lan_analysis:
            print("Both are equals, your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            wan_lan_close = list(set(wan_lan_analysis)-set(wan_lan_no_dmz))
            wan_lan_close.sort()
            print("wan->lan: ", wan_lan_close)
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

        if dmz_lan_wan == lan_wan_analysis:
            print("Both are equals, your network (lan->wan) was correctly configured")
        else:
            print("------------------")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            lan_wan_close = list(set(lan_wan_analysis) - set(dmz_lan_wan))
            lan_wan_close.sort()
            print("lan->wan: ", lan_wan_close)
        if dmz_wan_lan == wan_lan_analysis:
            print("Both are equals, your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            wan_lan_close = list(set(wan_lan_analysis) - set(dmz_wan_lan))
            wan_lan_close.sort()
            print("wan->lan: ", wan_lan_close)

        if dmz_wan_dmz == wan_dmz_analysis:
            print("Both are equals, your network (wan->dmz) was correctly configured")
        else:
            print("------------------")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            wan_dmz_close = list(set(wan_dmz_analysis) - set(dmz_wan_dmz))
            wan_dmz_close.sort()
            print("wan->dmz: ", wan_dmz_close)
        if dmz_dmz_wan == dmz_wan_analysis:
            print("Both are equals, your network (dmz->wan) was correctly configured")
        else:
            print("------------------")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            dmz_wan_close = list(set(dmz_wan_analysis) - set(dmz_dmz_wan))
            dmz_wan_close.sort()
            print("dmz->wan: ", dmz_wan_close)

        if dmz_dmz_lan == dmz_lan_analysis:
            print("Both are equals, your network (dmz->lan) was correctly configured")
        else:
            print("------------------")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            dmz_lan_close = list(set(dmz_lan_analysis) - set(dmz_dmz_lan))
            dmz_lan_close.sort()
            print("dmz->lan: ", dmz_lan_close)
        if dmz_lan_dmz == lan_dmz_analysis:
            print("Both are equals, your network (lan->dmz) was correctly configured")
        else:
            print("------------------")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            lan_dmz_close = list(set(lan_dmz_analysis) - set(dmz_lan_dmz))
            lan_dmz_close.sort()
            print("lan->dmz: ", lan_dmz_close)
    elif model == "3":
        checker = False
        print("Enter your Corporate Application port number: ")
        corp_app_port = int(input(prompt))
        #print("Enter your Database port number: ")
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
        wan_dmz_analysis.append(corp_app_port)
        wan_dmz_analysis.sort()

        print("Enter DMZ->WAN analysis path: ")
        reading = input(prompt)
        dmz_wan_analysis = xml_reading(reading)
        dmz_wan_analysis.append(corp_app_port)
        dmz_wan_analysis.sort()

        print("Enter DMZ->LAN analysis path: ")
        reading = input(prompt)
        dmz_lan_analysis = xml_reading(reading)
        dmz_lan_analysis.append(corp_app_port)
        dmz_lan_analysis.append(db_port)
        dmz_lan_analysis.sort()

        print("Enter LAN->DMZ analysis path: ")
        reading = input(prompt)
        lan_dmz_analysis = xml_reading(reading)
        lan_dmz_analysis.append(corp_app_port)
        lan_dmz_analysis.append(db_port)
        lan_dmz_analysis.sort()

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

        if dmz_lan_wan == lan_wan_analysis:
            print("Both are equals, your network (lan->wan) was correctly configured")
        else:
            print("------------------")
            print("Lan->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            lan_wan_close = list(set(lan_wan_analysis) - set(dmz_lan_wan))
            lan_wan_close.sort()
            print("lan->wan: ", lan_wan_close)
        if dmz_wan_lan == wan_lan_analysis:
            print("Both are equals, your network (wan->lan) was correctly configured")
        else:
            print("------------------")
            print("Wan->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            wan_lan_close = list(set(wan_lan_analysis) - set(dmz_wan_lan))
            wan_lan_close.sort()
            print("wan->lan: ", wan_lan_close)

        if dmz_wan_dmz == wan_dmz_analysis:
            print("Both are equals, your network (wan->dmz) was correctly configured")
        else:
            print("------------------")
            print("Wan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            wan_dmz_close = list(set(wan_dmz_analysis) - set(dmz_wan_dmz))
            wan_dmz_close.sort()
            print("wan->dmz: ", wan_dmz_close)
        if dmz_dmz_wan == dmz_wan_analysis:
            print("Both are equals, your network (dmz->wan) was correctly configured")
        else:
            print("------------------")
            print("Dmz->Wan analysis and recommended model are different")
            print("Vulnerability Level (DAM): Low")
            print("we recommend that you close the following ports: ")
            dmz_wan_close = list(set(dmz_wan_analysis) - set(dmz_dmz_wan))
            dmz_wan_close.sort()
            print("dmz->wan: ", dmz_wan_close)

        if app_dmz_lan == dmz_lan_analysis:
            print("Both are equals, your network (dmz->lan) was correctly configured")
        else:
            print("------------------")
            print("Dmz->Lan analysis and recommended model are different")
            print("Vulnerability Level (DAM): High")
            print("we recommend that you close the following ports: ")
            dmz_lan_close = list(set(dmz_lan_analysis) - set(app_dmz_lan))
            dmz_lan_close.sort()
            print("dmz->lan: ", dmz_lan_close)
        if app_lan_dmz == lan_dmz_analysis:
            print("Both are equals, your network (lan->dmz) was correctly configured")
        else:
            print("------------------")
            print("Lan->Dmz analysis and recommended model are different")
            print("Vulnerability Level (DAM): Medium")
            print("we recommend that you close the following ports: ")
            lan_dmz_close = list(set(lan_dmz_analysis) - set(app_lan_dmz))
            lan_dmz_close.sort()
            print("lan->dmz: ", lan_dmz_close)

    else:
        print("ERROR, select one valid option")
