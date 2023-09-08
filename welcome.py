from decouple import config
import requests

print(config("MY_PASSWORD"))