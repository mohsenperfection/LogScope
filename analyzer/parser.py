def read_logs(file_path):

    with open(file_path, "r") as file:

        for line in file:

            yield line.strip()



def parse_log_line(line):

    parts = line.split()

    if not parts:
        return None


    log_entry = {

        "ip": None,

        "endpoint": None,

        "status": None

    }


    if len(parts) > 0:
        log_entry["ip"] = parts[0]


    if len(parts) > 6:
        log_entry["endpoint"] = parts[6]


    if len(parts) > 8:
        log_entry["status"] = parts[8]


    return log_entry