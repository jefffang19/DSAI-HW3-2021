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

    for i in range(23):
        data.append([cur_date, "buy", 7 - i*0.1, 3+i])
        data.append([cur_date, "sell", 2.5 + i*0.1, 3+i])

        cur_date = get_last_date.next_hour(cur_date)
    return data
