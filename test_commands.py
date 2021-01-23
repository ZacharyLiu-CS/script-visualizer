import os

def exec_commands(commands:str) -> str:
    res = os.popen(commands)
    return res.read()
res_list = exec_commands("./scripts/meminfo.sh").strip().split("\n")
res_list = [float(i) for i in res_list]
print(res_list)
