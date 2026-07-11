class Metrics:

    def __init__(self):

        self.total_requests = 0

        self.unique_ips = set()



    def update(self, log):

        self.total_requests += 1


        ip = log.get("ip")

        if ip:

            self.unique_ips.add(ip)