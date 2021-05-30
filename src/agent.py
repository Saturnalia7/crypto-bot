import argparse
import pl
import socket



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--price', type=float)
    parser.add_argument('--entry', type=float)
    parser.add_argument('--capital', type=float)
    parser.add_argument('--ticker', type=str)
    return parser.parse_args()

args = get_args()
trade = pl.Trade(**vars(args))
trade.get_pl()
# print(trade)
# print(f'{pl}')