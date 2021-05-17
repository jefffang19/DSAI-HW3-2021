import get_last_date


def output(path, data):
    import pandas as pd

    df = pd.DataFrame(
        data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return


def generate_prediction(date):
    data = []

    cur_date = date

    for i in range(24):
        data.append([cur_date, "buy", 1, 1])
        data.append([cur_date, "sell", 2, 1])

        cur_date = get_last_date.next_hour(cur_date)
    return data
