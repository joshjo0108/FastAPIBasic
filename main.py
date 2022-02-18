# "FastAPI" PROVIDES ALL THE FUNCTIONALITY FOR YOUR API
from fastapi import FastAPI

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