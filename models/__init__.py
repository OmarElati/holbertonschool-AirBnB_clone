#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    storage = storage

storage = FileStorage()
storage.reload()

models_classes = {"BaseModel": BaseModel}
