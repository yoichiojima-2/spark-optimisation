from argparse import ArgumentParser
from datetime import datetime


def parse_args():
    parser = ArgumentParser()
    opt = parser.add_argument
    opt("--start-date", type=str, required=True)
    opt("--end-date", type=str, required=True)
    args = parser.parse_args()
    args.start_date = datetime.strptime(args.start_date, "%Y-%m-%d").date()
    args.end_date = datetime.strptime(args.end_date, "%Y-%m-%d").date()
    return args
