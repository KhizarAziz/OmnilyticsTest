from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
base_path = Path(__file__).parent.absolute()
file_path = base_path.joinpath('mFile.txt')

with open(file_path, "r") as mFile:
  text = mFile.read()
  text = text.replace(' ','')
  items = text.split(',')

def fetch(obj):
  if obj.isnumeric():
    res = f'{obj} - integer'
  elif obj.isalpha():
    res = f'{obj} - alphabetical strings'
  elif obj.isalnum():
    res = f'{obj} - alphanumeric'
  else:
    res = f'{obj} - real number'
  return res

pool = ThreadPoolExecutor(max_workers=15)

for j in pool.map(fetch, items):
  print(j)