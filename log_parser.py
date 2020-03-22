import pandas as pd
import re

dat_url = '/Users/rmaiale/dev/PythonFundamentals.Labs.RSVPAgentProcessingLogParser/data/rsvp_agent_log.dat'
print("WARNINGS:")
# dat_data = read(dat_url)
#
# print(dat_data)
with open(dat_url, "r+") as dat:
    for lines in dat:
        match = re.search("WARNING", lines)
        if match == None:
            pass
        else:
            print(str(lines.replace('\n\n', '\n')[0:14]) + " -- " + str(lines.replace('\n\n','\n')[45:]))
