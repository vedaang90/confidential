emp_id=["112233","445566"]
register_num=['4RABL','4RABM','4RABN','4RABO','4RANA','4RANB','4RABQ','4RABR','4RANC','4RAND','4RANE','4RANF','4RALA','4RALB','4RALC','4RALH','4RALJ','4RALS','4RALL','4RALM','4RALN','4RALO','4RALP','4RALQ','4RALR']
manufactur_type=['Airbus 320-232','Airbus 320-214','Airbus 320-214','Airbus 320-214','Airbus 320N-200','Airbus 320N-200','Airbus 321-231','Airbus 321-231','Airbus 321-251N','Airbus 321-251N','Airbus 321-251N','Airbus 321-251N','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-243','Airbus 330-300','Airbus 330-300','Airbus 330-343','Airbus 330-343','Airbus 330-343','Airbus 330-343','Airbus 330-343']
manufactur_name=['Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus','Airbus']
atd_icaq=['A320','A320','A320','A320','A20N','A20N','A321','A321','A21N','A21N','A21N','A21N','A332','A332','A332','A332','A332','A332','A333','A333','A333','A333','A333','A333','A333']
atd_iata=['320','320','320','320','32N','32N','321','321','32Q','32Q','32Q','32Q','32Q','332','332','332','332','332','332','333','333','333','333','333','333','333']
air_name=["ALR-457","BLR-257"]
air_type=["A330-300","B440-400"]
next_service=["20.4.22","20.5.22"]
prev_service=["20.4.20","20.5.20"]
check_type=["A","B"]
date=["20.4.21","20.5.21"]
fly_hours=["1000","2000"]
engineer=["Vedaang","Tom"]
command=["N","P","A","V"]
email=["ved-win@pm.me"]

print("Welcome to Aircraft Maintainance Portal")
id=input("Please enter your employee id:")
if id not in emp_id:
    print("Employee id not found, contact your manager!")
else:
    rn=input("Arcraft Registration Number:")
    if rn not in register_num:
        print("Registration Number not found..")
    else:
        i=register_num.index(rn)
        print('Aircraft Details:')
        print('Registration Number:',register_num[i])
        print('Manufacturer Type:',manufactur_type[i])
        print('Manufacturer Name:',manufactur_name[i])
        print('Aircraft Type Designator- ICAQ',atd_icaq[i])
        print('Aircraft Type Designator- IATA',atd_iata[i])

print('Thank you and we are improving our services')
        
