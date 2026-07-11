from analyzer.parser import read_logs, parse_log_line


def main():

    for line in read_logs("access.log"):

        log = parse_log_line(line)


        if log:

            print(log)

            break



if __name__ == "__main__":

    main()