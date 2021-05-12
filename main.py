import get_last_date
import generate_output
import read_input

# You should not modify this part.


def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./sample_data/consumption.csv",
                        help="input the consumption data path")
    parser.add_argument("--generation", default="./sample_data/generation.csv",
                        help="input the generation data path")
    parser.add_argument(
        "--bidresult", default="./sample_data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv",
                        help="output the bids path")

    return parser.parse_args()


if __name__ == "__main__":
    args = config()

    # read input dataframes
    consumption_df, generation_df, bidresult_df = read_input.read_input(
        args.consumption, args.generation, args.bidresult)

    # get current time
    last_date_time = get_last_date.get_current_date(consumption_df)

    # start predicting from next hour
    data = generate_output.generate_prediction(
        get_last_date.next_hour(last_date_time))

    # write result to output.csv
    generate_output.output(args.output, data)
