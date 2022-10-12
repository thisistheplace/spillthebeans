from pathlib import Path
import yaml
from yaml import CLoader as Loader

def read_file(fpath: str) -> bytes:
    resolved = Path(fpath).resolve()
    with open(resolved, "rb") as f:
        fbytes = f.read()
    return fbytes

def read_yaml(fpath: str) -> dict:
    resolved = Path(fpath).resolve()
    with open(resolved, "r") as f:
        yaml_dict = yaml.load(f, Loader)
    return yaml_dict