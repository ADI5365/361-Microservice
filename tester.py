# Microservice tester file

import time


while True:
    time.sleep(2.0)

    write_state_name = open("StateNames.txt", "w")
    write_state_name.write("Arizona")
    write_state_name.close()

    time.sleep(6.0)

    read_court_info = open("StateInfo.txt", "r")
    state_court_info = read_court_info.readline()
    read_court_info.close()

    print(state_court_info)
