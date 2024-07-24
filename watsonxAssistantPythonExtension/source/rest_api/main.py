# Dependencies
from fastapi import FastAPI  # Importing the FastAPI framework
import uvicorn  # Importing the uvicorn server
from pydantic import BaseModel  # Importing BaseModel for data validation

# Creating a FastAPI instance
app = FastAPI()

# Defining a Pydantic model for request validation
class NumbersRequest(BaseModel):
    number1: float
    number2: float

# Root endpoint for a GET request (test)
@app.get("/")
def read_root():
    return {"Hello": "World!"}

# Root to handle POST request for sum calculation
@app.post("/sum")
def sum(numbers: NumbersRequest):
    # Calculating the sum of the provided numbers
    result = numbers.number1 + numbers.number2
    # Retuing the sum of the provided numbers
    return {"result": result}

# Running the FastAPI application using uvicorn server
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)