saveyear=1930 #input one year before saveyear
for i in range(1931,1937): #1936 final
    saveyear += 1
    saveyearstring =str(saveyear)
    saveyearstring = "//Users//spitfirealeron//Desktop//code//hello //autosave_HKG_"+ saveyearstring + "_01_01.v2"

    f = open(saveyearstring, "r", encoding="ISO-8859-1")
    string = f.read()

    ########################################################################################################################
    ###############-----Hong Kong-------##########################################################################################

    start_index = string.index("1496=")
    end_index = string.index("1497=")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)
    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    # import csv
    # header = ['index','job','pop_id', 'population', 'ethnicity', 'money','literacy','prov_name', 'owner','date']
    # with open('popdata2.csv', 'w') as f:
    #    writer = csv.writer(f)
    #   writer.writerow(header)

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda

    # import csv
    # header = ['index','prov_name','owner', 'income', 'goods', 'date']
    # with open('provincedata2.csv', 'w') as f:
    #   writer = csv.writer(f)
    #  writer.writerow(header)

    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ########################################################################################################################
    ###############-----Singapore -------##########################################################################################

    start_index = string.index("1384=")
    end_index = string.index("1385=")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)
    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda
    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ########################################################################################################################
    ###############-----Penang -------##########################################################################################

    start_index = string.index("1388=")
    end_index = string.index("1389=")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)
    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda
    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ########################################################################################################################
    ###############-----Malacca -------##########################################################################################

    start_index = string.index("1386=")
    end_index = string.index("1387=")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)
    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda
    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ########################################################################################################################
    ###############-----Alor Setar -------##########################################################################################

    start_index = string.index("1389=")
    end_index = string.index("1390=")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)
    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda
    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ########################################################################################################################
    ###############-----Vancouver -------##########################################################################################

    start_index = string.index("13=\n")
    end_index = string.index("14=\n")
    a = int(start_index)
    b = int(end_index)
    hk_data = string[a:b]
    c = hk_data.replace("\t", " ")
    d = c.replace("\n", " ")

    import re

    prov_name_owner = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"'
    prov_name_owner = re.findall(prov_name_owner, d)
    [(name, owner)] = prov_name_owner

    prov_data1 = '([a-z]+)=  \{   id=(\d+)   size=(\d+)...([a-z]+.[a-z]+.[a-z]+|[a-z]+)=[a-z]+...money=(\d+\.\d+)'
    prov_data1 = re.findall(prov_data1, d)

    literacy = 'literacy=(\d+\.\d+)'
    literacy = re.findall(literacy, d)
    prov_income_goods = 'last_income=(\d+\.\d+)...goods_type=\"(\w+)\"'
    prov_income_goods = re.findall(prov_income_goods, d)
    [(income, goods)] = prov_income_goods
    dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
    date = re.findall(dateformula, string)
    date = str(date[0])

    # Writing pop csv using panda

    import pandas as pd

    data = prov_data1
    df = pd.DataFrame(data)
    df['literacy'], df['prov_name'], df['prov_owner'], df['date'] = literacy, name, owner, date
    df.rename(
        columns={
            df.columns[0]: 'job', df.columns[1]: 'pop_id', df.columns[2]: 'population', df.columns[3]: 'ethnicity',
            df.columns[4]: 'money'}, inplace=True)

    df.to_csv('popdata2.csv', mode='a', index=True, header=False)

    # writing prov csv using panda
    data = prov_name_owner
    dff = pd.DataFrame(data)
    dff["income"], dff["goods"], dff["date"] = income, goods, date
    dff.rename(
        columns={
            dff.columns[0]: "prov_name", dff.columns[1]: "prov_owner"}, inplace=True
    )
    dff.to_csv('provincedata2.csv', mode='a', index=True, header=False)

    ##################################################################################################################################
    # 19/2/22 extract yue data from world
    c = string.replace("\t", " ")
    d = c.replace("\n", " ")
    yue_data = 'date="(\d+.\d+.\d+)".player|name="(\w+.\w+.\w+)"..owner="(\w+)"|  ([a-z]+)=  \{   id=(\d+)   size=(\d+)...(yue)=[a-z]+...money=(\d+\.\d+).+?(?=literacy)literacy=(\d+\.\d+)'
    yue_data = re.findall(yue_data, d)

    # import csv
    # header = ['index','prov_name','owner', 'job', 'pop_id', 'population','ethnicity','money','date']
    # with open('yuedata2.csv', 'w') as f:
    #   writer = csv.writer(f)
    #  writer.writerow(header)

    # or?
    provcode = 0
    for i in range(1, 2703):  # 2703, 2702 is final
        provcode += 1
        provcodestring = str(provcode)
        provcodestring = provcodestring + "=\n"
        start_index = string.index(provcodestring)
        provcode2 = provcode + 1
        provcode2string = str(provcode2)
        provcode2string = provcode2string + "=\n"
        end_index = string.index(provcode2string)
        a = int(start_index)
        b = int(end_index)
        hk_data = string[a:b]
        c = hk_data.replace("\t", " ")
        d = c.replace("\n", " ")
        import re

        prov_data1 = 'name=\"((?:\w| )+)\"  owner=\"([\w]+)\"  |(\w+)=  {.  id=(\d+)   size=(\d+)   (yue)=\w+.  money=(\d+.\d+)'
        prov_data1 = re.findall(prov_data1, d)
        if len(prov_data1) == 1:
            continue
        # ('Johor Bahru', 'JOH', '', '', '', '', ''), ('', '', 'labourers', '15457', '232', 'yue', '613.14963')
        dateformula = 'date="(\d+.\d+.\d+)"\nplayer'
        date = re.findall(dateformula, string)
        date = str(date[0])
        import pandas as pd

        data = prov_data1
        df = pd.DataFrame(data)
        df['Date'] = date
        df.to_csv('yuedata2.csv', mode='a', index=True, header=False)

    # df.rename(
    #   columns={
    #      df.columns[0]: 'prov_name', df.columns[1]: 'owner', df.columns[2]: 'job', df.columns[3]: 'pop_id', df.columns[4]: 'population', df.columns[5]: 'ethnicity', df.columns[6]: 'money', df.columns[7]: 'date'}, inplace=True)


f.close()


