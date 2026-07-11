from analyzer.parser import read_logs, parse_log_line
from analyzer.metrics import Metrics



def main():

    metrics = Metrics()


    for line in read_logs("access.log"):

        log = parse_log_line(line)


        if log:

            metrics.update(log)



    print("=" * 40)
    print("LogScope Report")
    print("=" * 40)


    print(
        f"Total Requests: {metrics.total_requests}"
    )


    print(
        f"Unique IPs: {len(metrics.unique_ips)}"
    )



if __name__ == "__main__":

    main()