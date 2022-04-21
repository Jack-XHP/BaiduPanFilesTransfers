from bypy import ByPy
from bypy.util import get_pcs_path,print_pcs_list
bp=ByPy()
fmt='$t $f $s $m $d'
a=bp.list()
with open("downloaded.txt", "r") as file:
    savedUrl = file.readlines()
savedUrl1 = set(savedUrl)
for b in a:
    for i in range(len(b[3])):
        if b[3][i]['path']+'\n' in savedUrl1:
            continue
        savedUrl.append(b[3][i]['path']+"\n")
        with open("downloaded.txt", "w+") as file:
            if len(savedUrl) > 1000:
                savedUrl = savedUrl[-100:]
            file.write("".join(savedUrl))
        bp.downfile(b[3][i]['path'][11:], localpath=r"C:\Users\HomeNas\Downloads")
        bp.delete(b[3][i]['path'][11:])
        exit(0)
