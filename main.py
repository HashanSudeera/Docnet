import menu_module as menu
import main_module as main

ipcsv_file = "ip_info_save.csv"

while True:
    menu.main_menu()

    try:
        u_input = int(input("Enter the number for your choice :"))

        if u_input == 1:
            menu.random_ip_submenu()
        elif u_input == 2:
            menu.ip_info_submenu()
        elif u_input == 3:
            menu.sub_manager_submenu()
        elif u_input == 4:
            main.view_history(main.all_ip_info)
        elif u_input == 5:
            all_ip_list = main.all_ip_info
            main.ip_info_save(all_ip_list,ipcsv_file)
            print("Saved successfully! Check CSV file")
            continue
        elif u_input == 6:
            menu.help_submenu()
        elif u_input == 7:
            break
    
    except ValueError:
        print("Invalid input.Please Enter Valid Number.")

