# Matthew Tkachuk
# 2021/09/15
# .txt to .log converter


import os


def log_converter():
    log_path = 'C:\\Program Files (x86)\\Steam\\logs'   # Defaul log path
    new_log_path = ''   # INSERT DESIRED END LOCATION HERE

    if not os.path.exists(new_log_path):
        os.mkdir(new_log_path)

    for log in os.listdir(log_path):
        with open(os.path.join(log_path, log), 'r') as file:
            line = file.readlines()
            with open(os.path.join(new_log_path, (log[0:-4] + '.log')), 'w') as new_log:
                for x in line:
                    new_log.write(x)
                new_log.close()
            file.close()


log_converter()
