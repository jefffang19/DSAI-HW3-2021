def read_input(consumption, generation, bidresult):
    import pandas as pd

    cons_df = pd.read_csv(consumption)
    gene_df = pd.read_csv(generation)
    bid_df = pd.read_csv(bidresult)

    return cons_df, gene_df, bid_df
