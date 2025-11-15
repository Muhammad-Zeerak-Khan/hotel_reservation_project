import os 
import yaml
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException

import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try: 
        if not os.path.exists(file_path):
            raise FileNotFoundError("file is not present in the provided path.")            
