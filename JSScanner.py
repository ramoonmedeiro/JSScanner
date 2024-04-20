import concurrent.futures
import requests
from concurrent import futures
import argparse
import re
import urllib3
import colored
urllib3.disable_warnings()

argparser = argparse.ArgumentParser(description='JSScanner developed by 0x240x23elu (changed by Ramonstro)')
argparser.add_argument('--path', type=str, help='path for JS files.')
argparser.add_argument('--regex', type=str, help='Path for regex file.')
argparser.add_argument('--threads', type=int, help='Number of threads.')
argparser.add_argument('--output', type=str, help='Output file.')
args = argparser.parse_args()

path = args.path
reg = args.regex
threads = args.threads
output_file = args.output

print(colored.fg("red"),
     "╔════════════════════════════════════════════════════════════════╗\n"
      "║                    Devlope By 0x240x23elu                      ║\n"
      "║                     Changed by Ramonstro                       ║\n"
      "╚════════════════════════════════════════════════════════════════╝")
print("╔════════════════════════════════════════════════════════════════╗\n"
      "║                                                                ║\n"
      "║                           WARNING                              ║\n"
      "║                                                                ║\n"
      "║      I highly recommend using this tool by using Kali Linux OS ║\n"
      "║                                                                ║\n"
      "║      By using this tool it means you agree with terms,         ║\n"
      "║      conditions, and risks                                     ║\n"
      "║                                                                ║\n"
      "║      By using this tool you agree that                         ║\n"
      "║      1. use for legitimate security testing                    ║\n"
      "║      2. not for crime                                          ║\n"
      "║      3. the use of this tool solely for                        ║\n"
      "║         educational reasons only                               ║\n"
      "║                                                                ║\n"
      "║      By using this tool you agree that                         ║\n"
      "║      1. You are willing to be charged with criminal or state   ║\n"
      "║         law applicable by law enforcement officers             ║\n"
      "║         and government when abused                             ║\n"
      "║      2. the risk is borne by yourself                          ║\n"
      "║                                                                ║\n"
      "║         Thank you and happy pentest                            ║\n"
      "║                                                                ║\n"
      "╚════════════════════════════════════════════════════════════════╝")


list = []
file1 = open(path, 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    ip = line.strip()
    print(colored.fg("white"), ip)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(
                    lambda: requests.get(ip))
            for _ in range(1)
            ]

        results = [
            f.result().text
            for f in futures
        ]

        file2 = open(reg, 'r')
        Lines2 = file2.readlines()
        for line2 in Lines2:
            regex = line2.strip()
            matches = re.finditer(regex, str(results), re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                print(colored.fg("green"), "Regex: ", regex)
                print(colored.fg("red"), "Match {matchNum} was found at: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), '\n')
                f = open(output_file, 'a')
                L = [ip, '\n', "Regex: ", regex, '\n', "Match {matchNum} was found at : {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()),'\n']
                f.writelines(L)
                f.close()

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
