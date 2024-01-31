from crud_module import *
import requests

url = "https://jsonplaceholder.typicode.com/users"
datas = requests.get(url).json()

if __name__ == '__main__':
    # 회원추가
