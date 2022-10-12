from flask import Flask, make_response
from flask_restful import Resource, Api
from pathlib import Path

from ..constants import ASSETS_DIRECTORY
from ..system.fileutils import read_file

class StaticAsset(Resource):
    def __init__(self, path):
        self._path = path

    def get(self):
        response = make_response(read_file(self._path))
        response.headers["content-type"] = "application/text"
        return response

def add_assets(server: Flask, asset_names: list[str]):
    api = Api(server)
    for name in asset_names:
        asset_path = Path(f"{ASSETS_DIRECTORY}/{name}")
        if not asset_path.resolve().exists():
            raise FileNotFoundError(asset_path.resolve())
        # Dynamically create unique subclass since api.add_resource class must be unique type!
        SubClass = type(asset_path.stem, (StaticAsset,), {})
        api.add_resource(SubClass, "/" + str(asset_path), resource_class_args=[asset_path])