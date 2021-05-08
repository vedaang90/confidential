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
    
        
        
