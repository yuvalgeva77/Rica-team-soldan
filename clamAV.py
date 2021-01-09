import subprocess
import os
from os import path
from os.path import join
from os import chdir
from datetime import datetime


ROOT_DIR = path.dirname(path.dirname(__file__))
CWD = os.path.dirname(os.path.abspath(__file__))
DB_DIR = join(CWD, 'database')
REPORT_DIR = join(CWD, 'clamav\\report.txt')


# The function downloads the virus db to the folder
def download_virus_db():
    update_process = subprocess.Popen(["freshclam.exe"], cwd=CWD, shell=True)
    print("Downloading virus database. it could take a few minutes")
    update_process.wait()

def read_report_file():
    report_text = []
    with open(REPORT_DIR, 'r') as reader:
        line = reader.readline()
        while line != '':
            clean_line = line.strip()
            if clean_line:
                report_text.append(clean_line)
            line = reader.readline()
    return report_text

def parse_report(report_file):
    report = {}
    #add Known viruses
    data = report_file[2].split(':')
    report[data[0]] = data[1]
    # add scanned files
    data = report_file[5].split(':')
    report[data[0]] = data[1]
    # add infected files
    data = report_file[6].split(':')
    report[data[0]] = data[1]
    # add end date
    data = report_file[11].split(':', 1)
    report[data[0]] = data[1]
    return report


def create_report():
    report_file = read_report_file()
    report = parse_report(report_file)
    return report

# The function preform a scan and output result to file
def run_scan():
    # report_name = "report_" + ts_string + ".txt"
    # run_command = "clamscan.exe . --log=report.txt"
    # chdir("clamav")
    run_process = subprocess.Popen(["clamav\\clamscan.exe", "--log=report.txt"], cwd=CWD, shell=True)
    run_process.wait()
