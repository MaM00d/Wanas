
import pandas as pd
import torch
import json
#|%%--%%| <POlNBggkKd|mFdRwyniPb>

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

#|%%--%%| <mFdRwyniPb|G6ELBBiOzr>

with open("./qads/data/arcd-train.json", "r") as read_file:
    train = json.load(read_file)

#|%%--%%| <G6ELBBiOzr|q2Riyyjlbd>

train


#|%%--%%| <q2Riyyjlbd|IzkadVuc2u>

with open("./qads/data/arcd-test.json", "r") as read_file:
    test = json.load(read_file)

#|%%--%%| <IzkadVuc2u|YzxeX09vmO>


test

#|%%--%%| <YzxeX09vmO|QmDxSXhzi7>

data = pd.read_excel('/home/me/Projects/wana/langmod/wanas/ones/datasets/2.Egyptian Tweets.xlsx')
data["Text"].iloc[1]

#|%%--%%| <QmDxSXhzi7|1tcuIbHC1g>


# |%%--%%| <1tcuIbHC1g|MuxEQwUFSK>


