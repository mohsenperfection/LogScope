import sys
import os


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from analyzer.parser import parse_log_line
from analyzer.metrics import Metrics



def test_metrics_with_real_logs():


    logs = [

        '162.112.218.245 - - [01/Jun/2026:00:00:02 +0000] "GET /login HTTP/1.1" 200 8982 "-" "Mozilla/5.0"',


        '24.0.81.98 - - [01/Jun/2026:01:00:56 +0000] "GET /products/7197 HTTP/1.1" 200 878 "-" "Mozilla/5.0"',


        '43.181.159.78 - - [01/Jun/2026:01:56:30 +0000] "GET / HTTP/1.1" 200 11784 "-" "python-requests/2.31.0"',


        '45.157.54.134 - - [01/Jun/2026:02:55:54 +0000] "POST /login HTTP/1.1" 500 7232 "-" "Mozilla/5.0"',


        '169.16.177.109 - - [01/Jun/2026:03:42:04 +0000] "GET / HTTP/1.1" 404 3438 "-" "Mozilla/5.0"'

    ]


    metrics = Metrics()



    for line in logs:

        parsed = parse_log_line(line)

        if parsed:

            metrics.update(parsed)



    assert metrics.total_requests == 5


    assert len(metrics.unique_ips) == 5


    assert metrics.endpoints["/"] == 2


    assert metrics.endpoints["/login"] == 2


    assert metrics.products["7197"] == 1


    assert metrics.status_codes["200"] == 3


    assert metrics.status_codes["500"] == 1


    assert metrics.status_codes["404"] == 1


    assert round(metrics.error_rate(), 2) == 40.00