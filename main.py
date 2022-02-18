from enum import Enum

# "FastAPI" PROVIDES ALL THE FUNCTIONALITY FOR YOUR API
from fastapi import FastAPI

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

# CREATING AN INSTANCE OF THE CLASS "FastAPI"
# "app" IN "uvicorn main:app --reload" USED AS A VARIABLE
app = FastAPI()

# "path operations" IN FastAPI EVALUATED IN ORDER
# "/me" COULD BE MISCONSIDERED AS "{/item_id}"
@app.get("/users/me")
async def read_user_me():
  return {"user_id":"Jae Won Jo"}

# "get" IS ONE OF HTTP METHODS("OPERATIONS") TO PERFORM SPECIFIC ACTIONS
# "@" IS CALLED A DECORATOR, IT TAKES THE FUNCTION BELOW AND DOES SOMETHING WITH IT => "PATH("/") OPERATION("get") DECORATOR"
# OTHER OPERATORS ARE: .post(), .put(), .delete()
@app.get("/items/{item_id}")
# BELOW FUNCTION WILL BE CALLED BY "FastAPI" WHENEVER IT RECEIVES A REQUEST TO THE URL "/" USING A GET OPERATION.
# IF YOU ARE USING A "THIRD PARTY LIBRARIES" THAT TELL YOU TO CALL THEM WITH "await", DECLARE YOUR PATH OPERATION FUNCTIONS WITH "async def"
async def read_item(item_id: int):
  # ex) results = "await" some_library()
  # return results
  return {"item_id": item_id}

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
  if model_name == ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}
  # COULD ALSO ACCESS VIA USING "mdoel_name.lenet.value"
  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}
  return {"model_name": model_name, "message": "Have some residual"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
  return {"file_path" : file_path}