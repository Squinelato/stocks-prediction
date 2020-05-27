import pandas as pd

def select(csv_path):

    stocks = pd.read_csv(csv_path)

    mask = (stocks.TPMERC == 10) | (stocks.TPMERC == 20)

    selected_stocks = stocks.loc[mask, ['DATA DO PREGAO', 
                                        'PREABE', 
                                        'PREMAX', 
                                        'PREMIN', 
                                        'PREULT', 
                                        'VOLTOT']]

    selected_stocks.to_csv('selected_stocks.csv', index=False)
    
if __name__ == '__main__':
    select("stocks.csv")