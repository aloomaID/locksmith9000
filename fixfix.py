c=0
search_categories = open("/var/www/html/americanlocksmithsservice/duplicatescript1/staticfile/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
for credentials in search_categories:
    credential= credentials.strip().split(',')
    sub_ciy_repl= credential[0].title().replace('ï»¿', '')
    sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    short_code = credential[2].upper().replace('ï»¿', '')
    state_repl= credential[3].title().replace('ï»¿', '')
    state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    population= int(credential[8])
    zip_codes= credential[15]
    if 'Puerto Rico'.replace(' ', '-').lower() == state:
        continue
    elif 'Virgin Islands'.replace(' ', '-').lower() == state:
        continue
    elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
        continue
    elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
        continue
    elif 'American Samoa'.replace(' ', '-').lower() == state:
        continue
    elif 'Guam'.replace(' ', '-').lower() == state:
        continue
    elif 'Palau'.replace(' ', '-').lower() == state:
        continue
    elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
        continue
    elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
        continue
    elif 'Marshall Islands'.replace(' ', '-').lower() == state:
        continue
    elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
        continue
    else:
        pass

    if population < 1000:
        continue
    c +=1
    parent_dir2 = f"/var/www/html/locksmith9000/lockandkey/{state}/{sub_ciy}/index.html"
    search_categories = open(parent_dir2, "r", encoding="utf8").read()
    op= search_categories.replace("﻿", '').replace('aloomaid3', f'{sub_ciy_repl} {short_code}')
    
    fp = open(parent_dir2, "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
