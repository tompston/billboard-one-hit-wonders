# code
import pandas as pd

start_year = 1960
end_year = 2021

# download all of the data.
for year in range(start_year, end_year):
    
    # url uses the year as a parameter. Thus, changing the year in the url will return the appropriate billboard chart
    url = f'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}'
    table = pd.read_html(url)

    # holds the data
    df = table[0]

    # write the data of each year to a new csv file.
    file_path = f'./data/billboard_top_100_{year}.csv'
    df.to_csv(file_path, index=False)
