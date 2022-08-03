import os

global DIRECTORIES
global DIRECTORIES_PATH
DIRECTORIES = []
DIRECTORIES_PATH = []

def get_inputs() -> None:
  with open('input.txt', 'r') as f:
    inputs = f.readlines()
    for input in inputs:
      input = input.strip()
      print(input)
      directory_manager(input)

def directory_manager(input: list) -> None:
  input = input.split(' ')
  action = input[0]
  action = action.upper()   
  
  if action == 'LIST':
    list_directories()  
  elif action == 'CREATE':
    directory = input[1]
    create_directory(directory)
  elif action == 'DELETE':
    directory = input[1]
    delete_directory(directory)
  elif action == 'MOVE':
    current_path = input[1]
    target_path = input[2]
    move_directory(current_path, target_path)


def create_directory(directory:str) -> None:
  directory_list = directory.split('/')
  root = directory_list[0]
  if root not in DIRECTORIES:
    DIRECTORIES.append(directory_list[0])
    
  DIRECTORIES_PATH.append(directory)
  
  
def move_directory(current_path:str, target_path:str) -> None:
  valid_current_path = verify_directory(current_path)
  valid_target_path = verify_directory(target_path)
  if valid_current_path and valid_target_path:
    # if prefer not use os.path.basename in this challenge, can use basename=current_path.split('/')[-1]
    basename = os.path.basename(current_path)
    new_path = target_path+'/'+basename
    DIRECTORIES_PATH.append(new_path)
    DIRECTORIES_PATH.remove(current_path)
    if current_path in DIRECTORIES:
      DIRECTORIES.remove(current_path) 
      for idx, value in enumerate(DIRECTORIES_PATH):
        if current_path in DIRECTORIES_PATH[idx] and target_path not in DIRECTORIES_PATH[idx]:
          DIRECTORIES_PATH[idx] = target_path + '/' + DIRECTORIES_PATH[idx]
    else:
      for idx, value in enumerate(DIRECTORIES_PATH):
        DIRECTORIES_PATH[idx] = value.replace(current_path, target_path)
  

def delete_directory(directory:str) -> None:
  valid_directory = verify_directory(directory)
  if valid_directory:
    DIRECTORIES_PATH.remove(directory)
    if directory in DIRECTORIES:
      DIRECTORIES.remove(directory)
    for idx, value in enumerate(DIRECTORIES_PATH):
      if value.startswith(directory):
        DIRECTORIES_PATH.remove(value)


def verify_directory(directory:str) -> bool:
  valid_directory = True
  root = directory.split('/')[0]
  if root  not in DIRECTORIES:
    print(f'Cannot delete {directory} - {root} does not exist')
    valid_directory = False
  elif directory not in DIRECTORIES_PATH:
    print(f'Cannot delete {directory} - {directory} does not exist')
    valid_directory = False
  return valid_directory
  
  
def list_directories() -> None:
  DIRECTORIES_PATH.sort()
  # create directories dictionary from DIRECTORIES_PATH 
  directories_dict = {}
  for item in DIRECTORIES_PATH:
    temp = directories_dict 
    for x in item.split('/'):
      temp = temp.setdefault(x, {})
  print_directories(directories_dict)
  
  
def print_directories(directories_dict:dict, level=0) -> None:
  keys = directories_dict.keys()
  for key in keys:
    prefix = '  '*level
    print(f'{prefix}{key}', end='\n')
    if directories_dict.get(key):    
      obj = directories_dict.get(key)
      print_directories(obj, level+1)
  

get_inputs()
