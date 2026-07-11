from analyzer.parser import read_logs, parse_log_line
from analyzer.metrics import Metrics



def main():

    metrics = Metrics()


    processed_logs = 0


    for line in read_logs("access.log"):

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
        f"Total Requests: {metrics.total_requests}"
    )


    print(
        f"Unique IPs: {len(metrics.unique_ips)}"
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



    print("\nProcessed Logs:")
    print(processed_logs)



if __name__ == "__main__":

    main()