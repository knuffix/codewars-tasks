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


# print(get_common_directory_path(
#     ['lzarjg/azht/e/s/asd/fqwe', 'lzarjg/azht/e/s']))
# # /web
# print(get_common_directory_path(
#     ['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf']))
# print(get_common_directory_path(
#     ['/web/assets/style.css', '/.bin/mocha',  '/read.me']))
print(get_common_directory_path(
    [
        'trt/s/g/ysi/vbpswnsrsp/zpce/avmuvcclz/wqucikkbsk/yu/qnheeun/lsnsoqudp/zyn/cmi/gucqhg/quixiycdk/jkeaymiwk/mqxrcagg/zvrzilif/c/unkiixjuhn',
        # 'trt/s/g/ysi/vbpswnsrsp/zpcesarzw/bcljkilm',
        'trt/s/gffoogcddm/nvbsijcy/lxpyrakg/qt/twbdr/kgau/stryifbc/uevrs/g/hqiimhrdw/myvloxwxf/ajceqret/q/eu/wxjqpf/a/ccqivthx/easm',
        # 'trt/s/g/ysi/vbpswnsrsp/zpce/avmmmeco/ogatahld/mvwwtfyszj/fer/vnrmkau/tiodk/dqfb/dvihmgmdo/xe/noyxuhph/wayafmpvcc/uudp/ptq/cupxnttra/esmdfjd/f'
    ]))
# 'trt/s/g/' should equal 'trt/s/'
