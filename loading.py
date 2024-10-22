from tqdm import tqdm
from time import sleep

itens = range(100)
for i in tqdm(itens):
    sleep(0.01)