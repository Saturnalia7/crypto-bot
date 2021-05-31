



class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.tokens = {}


    def buy_token(self, ticker, token_price, capital):
        self.tokens[ticker].append()


class Trade:
    def __init__(self, ticker, entry, price, capital, currency='USD'):
        self.ticker = ticker
        self.currency = currency
        self.entry = entry
        self.capital = capital
        self.current_price = price
        pass

    def get_pl(self):
        self.delta = ((self.current_price - self.entry)/self.entry)
        self.pl =  self.delta * self.capital

        self.adj_delta = self.delta - 0.0016 * 2 # Kraken maker fee
        self.adj_pl = self.adj_delta * self.capital

        print(self.ticker)
        print(f'{self.pl:.7f}, {self.delta:.7f}')
        print(f'adjusted_pl:\n{self.adj_pl:.7f}, {self.adj_delta:.7f}\n')



        

# def main():
#     pass


# if __name__ == '__main__':
#     main()