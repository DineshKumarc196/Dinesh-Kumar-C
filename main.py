from app import main,get_prediction_from_url
from pandas import read_csv
from tqdm import tqdm


file_name = "Virus.csv"
dataframe = read_csv(file_name)
dataframe["result"] = ["Processing" for _ in dataframe["url"]]

bar = tqdm(total=len(dataframe["result"]),desc="Process")

# txt_file = open("result.txt","a") 
# with open("result.txt","xa") as txt_file:
for idx,url in enumerate(dataframe["url"]):
    dataframe["result"][idx] = get_prediction_from_url(url)
    # txt_file.write(str(f"{url},{get_prediction_from_url(url)}")+"\n")
    bar.update(1)
    dataframe.to_csv('result.csv')


