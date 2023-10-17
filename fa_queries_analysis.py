import os
import re
import pandas as pd
from texts_processing import TextsTokenizer


tokenizer = TextsTokenizer()

df = pd.read_csv(os.path.join("data", "queries.tsv"), sep="\t")
print(df)
print(df)
print(df.info())
print(df.describe())

df = df
df["QueryLen"] = df["query"].apply(lambda x: len(tokenizer([re.sub("\n", " ", x)])[0]))
df.to_csv(os.path.join("data", "fa_queries_with_len.csv"), sep="\t")