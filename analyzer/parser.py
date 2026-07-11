import gzip


def read_logs(file_path):

    if file_path.endswith(".gz"):

        file = gzip.open(file_path, "rt")

    else:

        file = open(file_path, "r")


    with file:

        for line in file:

            yield line.strip()





def parse_log_line(line):

    parts = line.split()


    if not parts:

        return None



    log_entry = {

        "ip": None,

        "endpoint": None,

        "status": None,

        "timestamp": None

    }




    if len(parts) > 0:

        log_entry["ip"] = parts[0]




    if len(parts) > 3:

        log_entry["timestamp"] = (

            parts[3]
            .replace("[", "")

        )




    if len(parts) > 6:

        log_entry["endpoint"] = parts[6]




    if len(parts) > 8:

        status = parts[8]

        if status.isdigit():

            log_entry["status"] = status




    return log_entry