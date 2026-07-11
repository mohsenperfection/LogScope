from collections import Counter


class Metrics:

    def __init__(self):

        self.total_requests = 0

        self.unique_ips = set()

        self.endpoints = Counter()

        self.products = Counter()

        self.status_codes = Counter()

        self.hourly_requests = Counter()

        self.error_count = 0



    def update(self, log):

        self.total_requests += 1


        ip = log.get("ip")

        if ip:

            self.unique_ips.add(ip)



        endpoint = log.get("endpoint")

        if endpoint:

            self.endpoints[endpoint] += 1


            product = self.extract_product(endpoint)

            if product:

                self.products[product] += 1



        status = log.get("status")

        if status:

            self.status_codes[status] += 1

            if status.startswith("4") or status.startswith("5"):

                self.error_count += 1

        hour = self.extract_hour(
            log.get("timestamp")
        )


        if hour:

            self.hourly_requests[hour] += 1





    def extract_product(self, endpoint):

        parts = endpoint.split("/")


        if "products" in parts:

            index = parts.index("products")


            if len(parts) > index + 1:

                return parts[index + 1]


        return None





    def extract_hour(self, timestamp):

        if not timestamp:

            return None


        try:

            return timestamp.split(":")[1]


        except IndexError:

            return None
        
    def error_rate(self):

        if self.total_requests == 0:

            return 0


        return (
            self.error_count /
            self.total_requests
    ) * 100