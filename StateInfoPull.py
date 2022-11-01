# User interface for microservice

import time
import json


while True:
    time.sleep(1.0)

    # read state name chosen by the user and save to variable
    read_state_name = open("StateNames.txt", "r")
    chosen_state_name = read_state_name.readline()
    read_state_name.close()

    # search for chosen state in JSON file
    with open("StateInformation.json", "r") as state_court_file:
        state_court_data = json.load(state_court_file)

        for state in state_court_data:
            if state == chosen_state_name:

                # write the chosen state's court info in StateInfo.txt
                overview = list(state_court_data[state].values())
                chosen_state_info = open("StateInfo.txt", "w")
                chosen_state_info.write(str(overview))

                chosen_state_info.close()

    state_court_file.close()
