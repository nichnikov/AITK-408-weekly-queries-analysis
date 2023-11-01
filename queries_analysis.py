import os
import re
import pandas as pd
from datetime import datetime
from texts_processing import TextsTokenizer


tokenizer = TextsTokenizer()

stopwords = []
for fn in ["greetings.csv", "stopwords.csv"]:
    stwrs_df = pd.read_csv(os.path.join(os.getcwd(), "data", fn), sep="\t")
    stopwords += list(stwrs_df["stopwords"])

tokenizer.add_stopwords(stopwords)

df = pd.read_csv(os.path.join("data", "queries42_43weeks_mondays.csv"), sep="\t")
print(df)
print(df.info())
print(df.describe())

# df["Date"] = df["Date"].apply(lambda x: datetime.strptime(re.sub("\.", "-", x), "%d-%m-%Y"))
# df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")
df["LemQueryLen"] = df["Query"].apply(lambda x: len(tokenizer([re.sub("\n", " ", x)])[0]))
print(df)
print(df.info())

df.to_csv(os.path.join("data", "queries42_43weeks_mondays_with_len.csv"), sep="\t", index=False)