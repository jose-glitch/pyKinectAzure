import os

folder = r"C:\Users\kraja\Queen Mary, University of London\EPSRC-2022 - radar_data"
#folder.replace("\","\\")
file_prefix = 'QMoffice01_'
file_date = '202301311141'
file_type = '.csv'

file_0 = os.path.join(folder, file_prefix+file_date+file_type)
print(file_0)
