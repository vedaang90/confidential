technician_id=["112233","445566"]
engineer_id=['334445','99901']
admin_name=['admin1','admin2']
admin_pass=['pwd1','pwd2']
register_num=['4RABL','4RABM','4RABN','4RABO','4RANA','4RANB','4RABQ','4RABR','4RANC','4RAND','4RANE','4RANF','4RALA','4RALB','4RALC','4RALH','4RALJ','4RALS','4RALL','4RALM','4RALN','4RALO','4RALP','4RALQ','4RALR']
manufactur_type=['Airbus 320-232','Airbus 320-214','Airbus 320-214','Airbus 320-214','Airbus 320N-200','Airbus 320N-200','Airbus 321-231','Airbus 321-231','Airbus 321-251N','Airbus 321-251N','Airbus 321-251N','Airbus 321-251N','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-300','Airbus 330-300','Airbus 330-343','Airbus 330-343','Airbus 330-343','Airbus 330-343','Airbus 330-343']
manufactur_name=['Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus']
atd_icaq=['A320','A320','A320','A320','A20N','A20N','A321','A321','A21N','A21N','A21N','A21N','A332','A332','A332','A332','A332','A332','A333','A333','A333','A333','A333','A333','A333']
atd_iata=['320','320','320','320','32N','32N','321','321','32Q','32Q','32Q','32Q','32Q','332','332','332','332','332','332','333','333','333','333','333','333','333']
next_service=["20.4.22","20.5.22"]
prev_service=["20.4.20","20.5.20"]
check_type=["A","B"]
date=["20.4.21","20.5.21"]
fly_hours=["1000","2000"]
technician=['tech1','tech2']
engineer=["Vedaang","Tom"]

def user_add():
    u=input('Type T to add Technician, E to add Engineer & A to add Admin:')
    if "T" in u:
        tech=input('Enter new Technician ID:')
        if tech in technician_id:
            print('Technician aldready exists.')
        else:
            technician_id.append(tech)
            print('Technician created.')
    elif "E" in u:
        eng=input('Enter new Engineer ID:')
        if eng in engineer_id:
            print('Engineer aldready exists.')
        else:
            engineer_id.append(eng)
            print('Engineer Created.')
    elif "A" in u:
        adm=input('Enter new Admin Username:')
        if adm in admin_name:
            print('Admin aldready exists.')
        else:
            pwd=input('Enter new Admin password:')
            admin_name.append(adm)
            admin_pass.append(pwd)
            print('Admin Created.')
def user_del():
    udel=input('Type T to delete Technician, E to delete Engineer & A to delete Admin.')
    if "T" in udel:
        delt=input('Enter Technician username:')
        technician_id.remove(delt)
        print('User Deleted.')
    elif "E" in udel:
        delt=input('Enter Engineer Username:')
        engineer_id.remove(delt)
        print('User Deleted.')
    elif "A" in udel:
        delt=input('Enter Admin Username:')
        index=admin_name.index(delt)
        if delt not in admin_name:
            print('Admin not found.')
        else:
            ps=input('Confirm Admin Password:')
            if ps in admin_pass:
                print('Incorrect Password.')
            else:
                admin_name.remove(delt)
                admin_pass.pop(index)
                print('Admin Deleted.')
    else:
        print('Invalid Command.')
def service_add():
    print('Fill the details below:')
    reg_no=input('Aircraft Registration Number:')
    manu_type=input('Manufacturer Type:')
    manu_name=input('Manufacturer Name:')
    iata=input('IATA Number:')
    icaq=input('ICAQ Number:')
    old_service=input('Previous Service Date:')
    service_date=input('Date of Service:')
    new_service=input('Next Service Date:')
    ct=input('Type of Check:')
    tec=input('Assigned Technician:')
    eng=input('Engiineer in charge:')
    register_num.append(reg_no)
    manufactur_type.append(manu_type)
    manufactur_name.append(manu_name)
    atd_iata.append(iata)
    atd_icaq.append(icaq)
    prev_service.append(old_service)
    next_service.append(new_service)
    date.append(service_date)
    check_type.append(ct)
    technician.append(tec)
    engineer.append(eng)
    print('Service Created Suuccesfully.')
def login():
    un=input('Please enter your username/employee id:')
    if un in technician_id:
        print('You are logged in as Technician.')
        
    elif un in engineer_id:
        print('You are logged in as Engineer.')
        
    elif un in admin_name:
        pw=input('Please enter your password:')
        no=admin_name.index(un)
        if admin_pass[no]==pw:
            print('You are logged in as Admin.')
            
        else:
            print('Incorrect Password.')
    else:
        print('User not found.')




print('Welcome to Aircraft Service Manegement Portal.')
login()
while 1<10:
    cmd=input('Press U to access user manager & S to access service manager:')
    if "U" in cmd:
        print('User Manager-')
        task=input('Press M to modify users & V to view users:')
        if "M" in task:
            t1=input('Press A to add users & D to delete users.')
            if "A" in t1:
                user_add()
            elif "D" in t1:
                user_del()
            else:
                print('Invalid Command.')
        elif "V" in task:
            print('Technicians:',technician_id)
            print('Engineers:',engineer_id)
            print('Admins:',admin_name)
        else:
            print('Invalid Command.')
    elif "S" in cmd:
        print('Service Manager-')
        task=input('Press A to add new service & V to view services.')
        if "A" in task:
            service_add()
        elif "V" in task:
            rn=input('Please enter the Aircraft Registration Number:')
            if rn not in register_num:
                print('Registration Number not found.')
            else:
                im=register_num.index(rn)
                print('Registration Number:',register_num[im])
                print('Manufacturer Type:',manufactur_type[im])
                print('Manufacturer Name:',manufactur_name[im])
                print('ATD-IATA:',atd_iata[im])
                print('ATD-ICAQ:',atd_icaq[im])
                print('Previous Service Details: Data Not Available')
                print('Date of Service: Data Not Available')
                print('Next Service: Data Not Available')
                print('Type of Check: Data Not Available')
                print('Engineer in charge: Data Not Available')
                print('Assigned Technician: Data Not Available')
        else:
             print('Invalid Command.')
print('Thank you for using our services.')             
        
        
