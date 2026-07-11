import argparse

from analyzer.parser import read_logs, parse_log_line
from analyzer.metrics import Metrics



def main():

    parser = argparse.ArgumentParser(
        description="LogScope - Log Analysis Tool"
    )


    parser.add_argument(
        "log_file",
        help="Path to log file"
    )


    args = parser.parse_args()


    log_path = args.log_file


    metrics = Metrics()


    processed_logs = 0


    for line in read_logs(log_path):

        log = parse_log_line(line)


        if log:

            metrics.update(log)

            processed_logs += 1



    print("=" * 50)
    print("              LogScope Report")
    print("=" * 50)



    print("\nGeneral Statistics")
    print("-" * 50)


    print(
        f"Total Requests : {metrics.total_requests}"
    )


    print(
        f"Unique IPs     : {len(metrics.unique_ips)}"
    )



    print("\nTop Endpoints")
    print("-" * 50)


    for endpoint, count in metrics.endpoints.most_common(10):

        print(
            f"{endpoint:<35} {count}"
        )



    print("\nTop Products")
    print("-" * 50)


    for product, count in metrics.products.most_common(10):

        print(
            f"Product {product:<25} {count}"
        )



    print("\nStatus Codes")
    print("-" * 50)


    for status, count in metrics.status_codes.items():

        print(
            f"{status}: {count}"
        )



    print("\nError Rate")
    print("-" * 50)


    print(
        f"{metrics.error_rate():.2f}%"
    )



    print("\nRequests Per Hour")
    print("-" * 50)


    for hour, count in sorted(
        metrics.hourly_requests.items()
    ):

        print(
            f"{hour}:00 -> {count}"
        )



    print("\nHourly Traffic Histogram")
    print("-" * 50)


    if metrics.hourly_requests:

        max_requests = max(
            metrics.hourly_requests.values()
        )


        for hour, count in sorted(
            metrics.hourly_requests.items()
        ):

            bar_length = int(
                (count / max_requests) * 50
            )


            bar = "#" * bar_length


            print(
                f"{hour}:00 | {bar} {count}"
            )



    print("\nSuspicious Login Attempts")
    print("-" * 50)


    suspicious_ips = metrics.get_suspicious_ips()


    if suspicious_ips:

        for ip, count in suspicious_ips.items():

            print(
                f"{ip:<25} {count} failed login attempts"
            )

    else:

        print(
            "No suspicious IPs detected"
        )



    print("\n5xx Error Spikes")
    print("-" * 50)


    error_spikes = metrics.detect_error_spikes()


    if error_spikes:

        for hour, rate in sorted(
            error_spikes.items()
        ):

            print(
                f"{hour}:00 -> Error Rate: {rate:.2f}%"
            )

    else:

        print(
            "No 5xx error spikes detected"
        )




if __name__ == "__main__":

    main()