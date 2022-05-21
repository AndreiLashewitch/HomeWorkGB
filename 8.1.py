import re
list_email = []
dict_info = {}
def email_parse(email_address):
    try:
        if email_address != ''.join((re.findall(r"\w+[@]\w+[/.]\w+", email_address))):
            raise ValueError()

    except ValueError:
        msg = 'wrong email {}'.format(str(email_address))
        raise ValueError(msg)

    else:
        val_1 = re.findall(r"\w+", email_address)
        val_2 = val_1[0]
        val_3 = re.findall(r'@\w+[/.]\w+', email_address)
        dict_info['username'] = val_2
        dict_info["domain"] = ''.join(val_3)


    return dict_info
#print(email_parse('andreilashewitch@icloud.com'))
print(email_parse('andrei.lashewitch@icloud.com'))