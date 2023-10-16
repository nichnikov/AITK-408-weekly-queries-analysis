import os
import re
import pandas as pd
from datetime import datetime
from texts_processing import TextsTokenizer


tokenizer = TextsTokenizer()
df = pd.read_csv(os.path.join("data", "queries41week.csv"), sep="\t")
print(df)
print(df.info())
print(df.describe())

df["Date"] = df["Date"].apply(lambda x: datetime.strptime(re.sub("\.", "-", x), "%d-%m-%Y"))
df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")
df["QueryLen"] = df["Query"].apply(lambda x: len(tokenizer([re.sub("\n", " ", x)])[0]))
print(df)
print(df.info())

df.to_csv(os.path.join("data", "queries41week_with_len.csv"), sep="\t")