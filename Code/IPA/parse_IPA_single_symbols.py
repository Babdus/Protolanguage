import sys
import pandas as pd
from collections import Counter

def main(argv):
    df = pd.io.parsers.read_csv(argv[0],index_col=0)
    # print(df)
    #
    # IPA_dict = {}
    # for i, row in df.iterrows():
    #     temp_dict = {}
    #     for col_name in row.index:
    #         print(i, col_name, row[col_name])
    #         if not pd.isnull(row[col_name]):
    #             temp_dict[col_name] = int(row[col_name])
    #     IPA_dict[i] = temp_dict
    # print(IPA_dict)
    print(df.columns.values.tolist())

    # df_dict_of_dicts = df.to_dict('index')
    # print(df_dict_of_dicts)
    # IPA_dict = {}
    # for df_dict in df_dict_of_dicts:
    #     IPA_dict[df_dict['Symbol']] =


if __name__ == "__main__":
    main(sys.argv[1:])
