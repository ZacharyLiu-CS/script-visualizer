#! /home/kvgroup/miniconda3/bin/python3
import asyncio
from pywebio import start_server, run_async
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, set_env, run_js
import os
import time
# 最大消息记录保存
MAX_MESSAGES_CNT = 10 ** 4


sys_cpu_usage = []
sys_mem_usage = []
sys_mem_cache = []
def exec_command(commands):
    res = os.popen(commands)
    return res.read()

def refresh_sysinfo():
    global sys_cpu_usage
    global sys_mem_usage
    global sys_mem_cache
    res_list = exec_command("./scripts/meminfo.sh").strip().split("\n")
    res_list = [float(i) for i in res_list]
    sys_cpu_usage.append(res_list[0])
    sys_mem_usage.append(res_list[1])
    sys_mem_cache.append(res_list[2])

async def main():
    global sys_cpu_usage
    global sys_mem_usage
    global sys_mem_cache
    set_env(title="View your Script Online")

    put_markdown("##Script Visualizer\n"
            "Monitor your system and manage your script", lstrip=True)

    msg_box = output()
    with use_scope('msg-container'):
        style(put_scrollable(msg_box, max_height=300), 'height:300px')

    # refresh_task = run_async(refresh_msg(nickname, msg_box))
    while True:
        time.sleep(1)
        refresh_sysinfo()
        msg_box.append(put_markdown('CPU Usage: %.2f, Mem Usage: %.2f, Mem Cache: %.2f'%(sys_cpu_usage[-1],sys_mem_usage[-1],sys_mem_cache[-1])))
        run_js('$("#pywebio-scope-msg-container>div").animate({ scrollTop: $("#pywebio-scope-msg-container>div").prop("scrollHeight")}, 1000)')  # hack: to scroll bottom



if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
