# https://www.codewars.com/kata/597f334f1fe82a950500004b/

def get_common_directory_path(pathes: list) -> str:
    tmp = pathes[0].split('/')
    for i in range(0, len(pathes)):
        tmp = common(tmp, pathes[i].split('/'))
    res = []
    for el_zero in pathes[0].split('/'):
        if el_zero in tmp:
            res.append(el_zero)
    if len(res) == 1 and res[0] == '':
        return '/'
    if not len(res):
        return ''
    res = '/'.join(res)
    res += '/'
    for path in pathes:
        if path == res[:len(res) - 1]:
            res = res[:len(res) - 1]
    return res


def common(lst1, lst2):
    res = []
    for i in range(0, len(lst1)):
        for j in range(0, len(lst2)):
            if lst1[i] == lst2[j]:
                res.append(lst1[i])
                break
            if j > i:
                break
    return res