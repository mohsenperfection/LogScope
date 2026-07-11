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


        # Failed login detection
        self.failed_login_ips = Counter()


        # 5xx error detection
        self.hourly_5xx_errors = Counter()



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


            # General error counting
            if status.startswith("4") or status.startswith("5"):

                self.error_count += 1



            # Failed login detection

            if (
                endpoint == "/login"
                and status == "401"
                and ip
            ):

                self.failed_login_ips[ip] += 1




            # 5xx error tracking

            if status.startswith("5"):

                hour = self.extract_hour(
                    log.get("timestamp")
                )

                if hour:

                    self.hourly_5xx_errors[hour] += 1





        # Requests per hour

        hour = self.extract_hour(
            log.get("timestamp")
        )


        if hour:

            self.hourly_requests[hour] += 1





    def get_suspicious_ips(self, threshold=5):

        suspicious = {}


        for ip, count in self.failed_login_ips.items():

            if count >= threshold:

                suspicious[ip] = count


        return suspicious





    def detect_error_spikes(self, threshold=10):

        spikes = {}


        for hour, requests in self.hourly_requests.items():


            errors = self.hourly_5xx_errors.get(
                hour,
                0
            )


            if requests == 0:

                continue



            error_rate = (
                errors /
                requests
            ) * 100



            if error_rate > threshold:

                spikes[hour] = round(
                    error_rate,
                    2
                )


        return spikes





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