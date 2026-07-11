from collections import Counter


class Metrics:

    def __init__(self):

        self.total_requests = 0

        self.unique_ips = set()

        self.endpoints = Counter()

        self.products = Counter()

        self.status_codes = Counter()



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





    def extract_product(self, endpoint):

        parts = endpoint.split("/")


        if "products" in parts:

            index = parts.index("products")


            if len(parts) > index + 1:

                return parts[index + 1]


        return None