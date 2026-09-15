from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from pydantic import BaseModel

app = FastAPI()

# Configure the templates directory relative to this file
templates = Jinja2Templates(directory="src/templates")

# Temporary in-memory list to store items
items_list = []

# Define a class (Pydantic model) for the data structure
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Route to list all data (GET)
@app.get("/items/")
def get_items():
    return items_list



# 1. Serve the HTML Template (GET)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Pass the 'request' context variable—FastAPI requires this for Jinja2
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"items": items_list}
)
    


# ---- CHANGE THIS ENDPOINT TO ACCEPT FORM DATA ----
@app.post("/items/")
def create_item(
    name: str = Form(...), 
    description: str = Form(None), 
    price: float = Form(...), 
    tax: float = Form(None)
):
    new_item = {
        "name": name,
        "description": description if description else None,
        "price": price,
        "tax": tax if tax else 0.0
    }
    items_list.append(new_item)
    
    # Redirect back to the home page so the list refreshes automatically
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)