import sys
import os
import psutil
import time
import math
import platform

from api import message
from api.bot import Bot

from libs import readableTime, displayname

def convert_size(size_bytes):
    if size_bytes == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes/p, 2)
    return '%s %s' % (s, size_name[i])

async def run(message_in):
    # Get information about host environment.
    time_current = int(time.time())

    # CPU stats.
    cpu_threads = os.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory stats.
    mem_stats = psutil.virtual_memory()
    mem_percent = mem_stats.percent
    mem_used = convert_size(mem_stats.used)
    mem_total = convert_size(mem_stats.total)

    # Platform info.
    platform_current = platform.platform()

    # Python version info.
    pyver_major = sys.version_info.major
    pyver_minor = sys.version_info.minor
    pyver_micro = sys.version_info.micro
    pyver_release = sys.version_info.releaselevel

    # Storage info.
    stor = psutil.disk_usage('/')
    stor_used = convert_size(stor.used)
    stor_total = convert_size(stor.total)
    stor_free = convert_size(stor.total - stor.used)

    # Format hostinfo with OS, CPU, RAM, storage, and other bot info.
    msg = '***{}\'s*** **Home:**\n'.format(displayname.name(message_in.server.me))
    msg += '```Host OS       : {}\n'.format(platform_current)
    msg += 'Host Python   : {}.{}.{} {}\n'.format(pyver_major, pyver_minor, pyver_micro, pyver_release)
    if not isinstance(cpu_threads, int):
        msg += 'Host CPU usage: {}% of {}\n'.format(cpu_usage, platform.machine())
    elif cpu_threads > 1:
        msg += 'Host CPU usage: {}% of {} ({} threads)\n'.format(cpu_usage, platform.machine(), cpu_threads)
    else:
        msg += 'Host CPU usage: {}% of {} ({} thread)\n'.format(cpu_usage, platform.machine(), cpu_threads)

    msg += 'Host RAM      : {} ({}%) of {}\n'.format(mem_used, mem_percent, mem_total)
    msg += 'Host storage  : {} ({}%) of {} - {} free\n'.format(stor_used, stor.percent, stor_total, stor_free)
    msg += 'Hostname      : {}\n'.format(platform.node())
    msg += 'Host uptime   : {}```'.format(readableTime.getReadableTimeBetween(psutil.boot_time(), time.time()))

    # Return completed message.
    return message.Message(body=msg)