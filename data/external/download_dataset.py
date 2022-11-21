import requests
import os


def download_dataset():
    if not os.path.exists('../../raw'):
        os.makedirs('data/raw')
        response = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data')
        with open('data/raw/magic04.data', 'wb') as f:
            f.write(response.content)
    else:
        print('Raw data already exists')


if __name__ == '__main__':
    download_dataset()
