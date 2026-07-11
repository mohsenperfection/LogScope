# LogScope

LogScope is a simple command line tool for analyzing server log files.

The purpose of this project is to read log files and collect useful information such as request count, status codes, IP addresses, endpoints and suspicious activities.

The program reads logs line by line instead of loading the whole file into memory. This makes it possible to process large log files.

## About This Project

This project was developed as part of the internship entrance task at Hamravash.

## Features

- Count total requests
- Count unique IP addresses
- Find popular endpoints
- Count HTTP status codes
- Show requests per hour
- Detect high number of 5xx errors
- Detect suspicious failed login attempts
- Support normal log files and gzip compressed log files

## Requirements

- Python 3.10+

No external packages are required.

## Project Structure

```text
LogScope/
│
├── main.py
│
├── analyzer/
│   ├── parser.py
│   └── metrics.py
│
├── tests/
│
└── README.md
```

## How to Run

Run the program with the log file path:

```bash
python main.py access.log
```

Example:

```bash
python main.py sample.log
```

For compressed log files:

```bash
python main.py sample.log.gz
```

## Example Log Format

The parser works with common web server log format.

Example:

```text
50.51.126.254 - - [01/Jun/2026:00:06:58 +0000] "GET /products HTTP/1.1" 200 1234
```

The program extracts information such as:

- IP address
- Request method
- Endpoint
- Status code
- Timestamp

## Output Example

```text
Total requests: 50000

Unique IPs: 1200

Top endpoints:
 /api/login 1200
 /products 900

Status codes:
200 : 45000
404 : 3000
500 : 500

Suspicious activity:
IP 192.168.1.10 had many failed login attempts

5xx spike detected:
Hour 14:00 - 12% errors
```

## Libraries

This project only uses Python standard libraries.

No external package is used for parsing logs. The log parsing logic is implemented manually inside the project.

### argparse

Used to create the command line interface and receive the log file path from the user.

### collections

Used for storing and counting statistics.

`Counter` is used for counting:

- Status codes
- Endpoints
- Failed login attempts
- Requests per hour

### gzip

Used for reading compressed `.gz` log files.

Many server logs are compressed to reduce storage size, so this library allows the program to analyze them directly without extracting them first.

### os

Used for file path and file related operations.

### sys

Used for accessing system information and handling program execution.

### time

Used to measure the execution time of the program.

## External Libraries

No third-party libraries are used.

A library that automatically parses server logs was not used because the parsing logic is implemented manually in this project.

## Project Design

The project is divided into two main parts:

### Parser

The parser reads each log line and extracts required information.

### Metrics

The metrics module receives parsed logs and calculates different statistics.

This separation makes it easier to add new features in the future.
