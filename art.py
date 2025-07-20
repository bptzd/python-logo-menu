from pystyle import Colors, Colorate, Center

logo = r'''
██╗      ██████╗  ██████╗  ██████╗ 
██║     ██╔═══██╗██╔════╝ ██╔═══██╗
██║     ██║   ██║██║  ███╗██║   ██║
██║     ██║   ██║██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝
'''

menu_box = r"""
╔═════════════════════════════╗
║         Main Menu           ║
╠═════════════════════════════╣
║  1. Example1                ║
║  2. Example2                ║
║  3. Example3                ║
╚═════════════════════════════╝
"""

colored_logo = Center.XCenter(Colorate.Vertical(Colors.red_to_yellow, logo, 3))

try:
    colored_menu = Center.XCenter(Colorate.Vertical(Colors.red_to_orange, menu_box, 3))
except AttributeError:
    colored_menu = Center.XCenter(Colorate.Vertical(Colors.red_to_yellow, menu_box, 3))

print(colored_logo)
print(colored_menu)
print(Center.XCenter("bot"))
print(Center.XCenter("Choose Option (1/2/3): "))
choice = input()
print(f"\nYou selected option {choice}")
