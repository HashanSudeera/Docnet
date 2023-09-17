import main_module as ipmain


# Main Menu 

def main_menu():
    print('''

==========================================================================
 
        ▀███▀▀▀██▄                 ▀███▄   ▀███▀         ██        ██
          ██    ▀██▄                 ███▄    █           ██      ██████  
          ██     ▀██ ▄██▀██▄ ▄██▀██  █ ███   █   ▄▄█▀████████      ██
          ██      ████▀   ▀███▀  ██  █  ▀██▄ █  ▄█▀   ██ ██        
          ██     ▄████     ███       █   ▀██▄█  ██▀▀▀▀▀▀ ██   
          ██    ▄██▀██▄   ▄███▄    ▄ █     ███  ██▄    ▄ ██   
        ▄████████▀   ▀█████▀ █████▀▄███▄    ██   ▀█████▀ ▀████
                                                                                                 
==========================================================================
        [1] = Random Ip Generator
        [2] = IP Address Info
        [3] = Subnet Manager
        [4] = View ip history
        [5] = Save 
        [6] = Help & About
        [7] = Exit
==========================================================================
          ''',)




# Option 1 : Random ip generator [sub menu]

def random_ip_submenu ():
    print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         _                   ___ _     __                        
        |_) _  _  _| _ __     | |_)   /__ _  _  _   _ _ _|_ _   _
        | \(_|| |(_|(_)|||   _|_|     \_|(/_| |(/_ | (_| |_(_) | 
          
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    [1] = Generate Random IP Address
    [2] = Generate Random IP Specific for class
    [0] = Back to Main menu
''')
    
    while True:
        try:
            u_input = int(input("Enter the number for your choice :")) 

            if u_input == 1:
                ipmain.random_ip()
            elif u_input == 2:
                ipmain.random_ip_class()
            elif u_input == 0:
                break
        
        except ValueError:
            print("Invalid input.Please Enter Valid Number.")



# Option 2 : IP Address Info
def ip_info_submenu():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ___ _     _                      ___     _   
         | |_)   |_| _| _|  _ _  _  _     |  _ _|_ _ 
        _|_|     | |(_|(_| | (/__> _>    _|_| | | (_)
          
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
    
    ipmain.ip_info(ipmain.all_ip_info)



# Option 3 : Subnet Manager
def sub_manager_submenu():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
             __                               _       
            (_    |_  _  _ _|_   |V| _  _  _ (_| _   _
            __)|_||_)| |(/_ |_   | |(_|| |(_|__|(/_ | 
          
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    [1] = Fixed lenght subnet mask (FLSM)
    [0] = Back to Main menu              
''')


# Option 6 : Help & About
def help_submenu():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
                                            
            |_| _ ||_)    _  _  _|   |_||_  _    _|_
            | |(/_||     (_|| |(_|   | ||_)(_)|_| |_
          
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    [1] = Help
    [2] = About
    [0] = Back to main menu 
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice :")) 

            if u_input == 1:
                help()
            elif u_input == 2:
                about()
            elif u_input == 0:
                break
        
        except ValueError:
            print("Invalid input.Please Enter Valid Number.")
    
    

# Description about our team and instructions...
def about():
    print('''
                         
        |=================================== < We Are > ======================================|
        |         ___   _     _         _            ___                         _            |
        |        (  _ \(_ ) _( )_      ( )          (  _ \                      ( )           |
        |        | ( (_)| |(_)  _)  ___| |__  ______| (_(_)  _ _ _   _   _ _   _| |           |  
        |        | | __ | || | |  / ___)  _  \______)\__ \ / _  ) ) ( )/ _  )/ _  |           |  
        |        | |(_ )| || | |_( (___| | | |      ( )_) | (_) | (_) | (_| | (_| |           |
        |        (____/(___)_)\__)\____)_) (_)       \____)\__  |\___/ \__ _)\__ _)           | 
        |                                                    | |                              |
        |                                                    (_)                              |
        |================================== < Developers > ===================================|
        |                                                                                     |       
        |                                                                                     | 
        |                                                                                     |      
        |        </> Umesh (TraKa) - The Front-End Magician:[Leader]                          |
        |            - Umesh crafts interfaces and solves design challenges,                  |
        |            making websites and apps shine.                                          |
        |                                                                                     |  
        |                                                                                     |  
        |        </> Sudeera (Sudda) - The Back-End Wizard:                                   |
        |            - Sudeera powers the behind-the-scenes magic, making smooth              |
        |            operations and functionality.                                            |
        |                                                                                     |  
        |                                                                                     |                  
        |        </> Nimuthu (PP) - The Front-End Helper:                                     |    
        |            - Nimuthu brings designs to life and keeps us updated with the           |
        |            latest tech trends, making sure everything runs seamlessly.              |
        |                                                                                     |                  
        |                                                                                     |              
        |                                                                                     |              
        |=====================================================================================|
        |            Together, we are the Glitch Squad, reshaping industry                    |
        |            learning through our unique skills and teamwork.                         |
        |=====================================================================================|
        |               _____ _                 _       _     _               _               |
        |              (_   _) )               ( )     ( )   ( )             ( )              |
        |                | | | |__    _ _  ___ | |/ )   \ \_/ /   _   _   _  | |              |
        |                | | |  _  \/ _  )  _  \   (      \ /   / _ \( ) ( ) | |              |
        |                | | | | | | (_| | ( ) | |\ \     | |  ( (_) ) (_) | (_)              |  
        |                (_) (_) (_)\__ _)_) (_)_) (_)    (_)   \___/ \___/                   |
        |                                                                    (_)              |                                                            
        |=====================================================================================|                                                        
                                                                            



''')



def help ():
    print('''
               |=================================================================|
               |         ╔══╗         ╔╗             ╔╗                          |
               |         ╚╣╠╝        ╔╝╚╗           ╔╝╚╗                         |
               |          ║║ ╔═╗ ╔══╗╚╗╔╝╔═╗╔╗╔╗╔══╗╚╗╔╝╔╗╔══╗╔═╗ ╔══╗           |
               |          ║║ ║╔╗╗║══╣ ║║ ║╔╝║║║║║╔═╝ ║║ ╠╣║╔╗║║╔╗╗║══╣           |
               |         ╔╣╠╗║║║║╠══║ ║╚╗║║ ║╚╝║║╚═╗ ║╚╗║║║╚╝║║║║║╠══║           |
               |         ╚══╝╚╝╚╝╚══╝ ╚═╝╚╝ ╚══╝╚══╝ ╚═╝╚╝╚══╝╚╝╚╝╚══╝           |
        =======|=================================================================|======|
        |                                                                               |
        |       Absolutely, let's simplify the descriptions for better understanding:   |
        |                                                                               |
        |                                                                               |
        |           1. Random IP Generator:                                             |
        |               - Make random fake IP addresses for practicing or learning.     |
        |                                                                               |
        |           2. IP Address Info:                                                 |
        |               - Learn about where an IP is from and who uses it.              |
        |                                                                               |
        |           3. Subnet Manager:                                                  |
        |               - Organize and handle groups of IP addresses easily.            |
        |                                                                               |
        |           4. View IP History:                                                 |
        |               - See a list of IP addresses you've used before.                |
        |                                                                               |
        |           5. Save:                                                            |
        |               - Keep important IP addresses or settings for later.            |
        |                                                                               |
        |           6. Help & About:                                                    |
        |               - Get instructions and find out about our team.                 |
        |                                                                               |
        |           7. Exit:                                                            |
        |               - Close the project when you're done using it.                  |
        |                                                                               |
        |                                                                               |
        |===============================================================================|
''')
    
            




