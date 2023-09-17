# ramdom module 
import random as ran
# ipaddress module
import ipaddress as ipa
#save csv module import
import csv

all_ip_info = []

#This is yer or no continue function
def y_n_continue():
    while True:
            u_choice = str(input("Do you want to continue(y/n) :"))

            if u_choice == 'y' or u_choice == 'Y':
                return True
            elif u_choice == 'n' or u_choice == 'N':
                return False                
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

def ip_info_save(ip_list:list,file):
    
    title = [[["IP ADDRESS"],["NETWORK ADDRESS"],["BROADCAST ADDRESS"],["DEFULT MASK"],["IP VERSION"],["NUMBER OF HOSTS"]]]
    with open(file, "a", newline= '') as ip_info_save:
        writer = csv.writer(ip_info_save)
        writer.writerows(title)
        writer.writerows(ip_list)


# [1] random ip genarator function
def random_ip():

    while True:
        try:
            u_input = int(input("How much ip addresses do you want? : "))

            all_ip = []

            for j in range(u_input):
                ip_address = []
                for i in range(4):
                    num = ran.randint(0,255)
                    ip_address.append(num)

                all_ip.append(ip_address)
            
            count = 1
            for ip in all_ip:    
                num1 = ip[0]
                num2 = ip[1]
                num3 = ip[2]
                num4 = ip[3]

                print(f"ip_address {count} = [{num1}.{num2}.{num3}.{num4}]")
                count += 1
        except ValueError:
            print("Invalid input.Please Enter Valid Number.")
            continue
        
        choice = y_n_continue()

        if choice == True:
            continue
        elif choice == False:
            break
        else:
            y_n_continue()

def random_ip_class():
    while True:
        try:
            clss = str(input("Class(A,B,C,D,E) :"))
            count = int(input("How much ip addresses do you want? : "))

            all_ip = []

            for j in range(count):
                if clss == 'A' or clss == 'a':
                    start = 0
                    end = 127
                elif clss == 'B' or clss == 'b':
                    start = 128
                    end = 191
                elif clss == 'C' or clss == 'c':
                    start = 192
                    end = 223
                elif clss == 'D' or clss == 'd':
                    start = 224
                    end = 239
                elif clss == 'E' or clss == 'e':
                    start = 240
                    end = 255
                
                first_8bit = []
                for i in range(1):
                    num = ran.randint(start,end)
                    first_8bit.append(num)
                
                ip_address = []
                for i in range(3):
                    num = ran.randint(0,255)
                    ip_address.append(num)

                all_ip.append(first_8bit+ip_address)
            
            count = 1
            for ip in all_ip:    
                num1 = ip[0]
                num2 = ip[1]
                num3 = ip[2]
                num4 = ip[3]

                print(f"ip_address {count} = [{num1}.{num2}.{num3}.{num4}]")
                count += 1
        except ValueError:
            print("Invalid input.Please Enter Valid Number.")
            continue
        
        choice = y_n_continue()

        if choice == True:
            continue
        elif choice == False:
            break
        else:
            y_n_continue()

#[2] IP info function
def ip_info(all_iplist:list):
    

    while True:

        ip_info = []

        get_ip = input("Enter ip address :")

        try:
            ipa.ip_address(get_ip)

        except ValueError:
            print("Invalid ip address")
            continue

        ip_part = get_ip.split(".")
        #['6','34','56','0']

        first_part = int(ip_part[0])

        #class A
        if first_part >= 0 and first_part <= 127:
            fix_bit = '/8'
            clss = 'A'

        #class B
        elif first_part >= 128 and first_part <= 191:
            fix_bit = '/16'
            clss = 'B'

        #class C
        elif first_part >= 192 and first_part <= 223:
            fix_bit = '/24'
            clss = 'C'

        #class D
        elif first_part >= 224 and first_part <= 239:
            fix_bit = '/24'
            clss = 'D'

        #class E
        elif first_part >= 240 and first_part <= 255:
            fix_bit = '/24'
            clss = 'E'

        use_ip = ipa.ip_interface(get_ip+fix_bit)

        n_a = use_ip.network.network_address
        b_a = use_ip.network.broadcast_address
        d_mask = use_ip.network.netmask
        version = use_ip.network.version
        num_address = use_ip.network.num_addresses
        

        print('''
  +-----------------------------------------+
  |          Ip Address Infomation          |                    
  +-----------------------------------------+''')
                
        print(f"    > Network address  | {n_a}      ")
        print("  |-----------------------------------------|")
        print(f"    > Broadcat address | {b_a}    ")         
        print("  |-----------------------------------------|")
        print(f"    > Defult mask      | {d_mask}      ")       
        print("  |-----------------------------------------|")
        print(f"    > Class            | {clss}                 ")
        print("  |-----------------------------------------|")
        print(f"    > IP Version       | {version}                 ")
        print("  |-----------------------------------------|")
        print(f"    > Number of hosts  | {num_address}              ")
        print("  +-----------------------------------------+")
        print(" ")

        # append ip info for list
        ip_info.append(get_ip)
        ip_info.append(str(n_a))
        ip_info.append(str(b_a))
        ip_info.append(str(d_mask))
        ip_info.append(str(version))
        ip_info.append(str(num_address))

        all_iplist.append(ip_info)


        choice = y_n_continue()

        if choice == True:
            continue
        elif choice == False:
            break
            
        else:
            continue

def view_history(ip_list:list):

    print('''
  +-----------------------------------------------------------------------------------------------------------+
  |    Ip Address    |     Network Address  | Broadcast Address |  Defult Mask    |   Version   | Num Address |                 
  +-----------------------------------------------------------------------------------------------------------+''')

    for ip_info in ip_list:
        print(f'{ip_info[0]}  | {ip_info[1]} | {ip_info[2]} | {ip_info[3]} | {ip_info[4]} | {ip_info[5]} |')
        print("|-----------------------------------------------------------------------------------------------------|")
    while True:
        u_choice = input("[0] Back to Main menu : ")

        if u_choice != '0':
            print("invalid input")
            continue

        if u_choice == '0':
            break

def subnet_maneger():
    while True:

        ip_info = []

        get_ip = input("Enter ip address :")

        try:
            ipa.ip_address(get_ip)

        except ValueError:
            print("Invalid ip address")
            continue

        
        
        
        

        
        




    

        

            



