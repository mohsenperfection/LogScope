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



def test_parse_real_log_line():


    line = (
        '162.112.218.245 - - '
        '[01/Jun/2026:00:00:02 +0000] '
        '"GET /login HTTP/1.1" '
        '200 8982 "-" '
        '"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"'
    )


    result = parse_log_line(line)


    assert result["ip"] == "162.112.218.245"

    assert result["endpoint"] == "/login"

    assert result["status"] == "200"

    assert result["timestamp"] == "01/Jun/2026:00:00:02"