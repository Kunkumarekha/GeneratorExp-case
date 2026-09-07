from fastapi import FastAPI

app = FastAPI()

# Supermarket inventory API (Application Programming Interface) with CRUD operations

items = ["Rice", "Toor Dal", "Sugar", "Cooking Oil", "Biscuits"]
prices = [60.0, 120.0, 55.0, 150.0, 30.0]
stock = [50, 30, 40, 25, 60]


# GET - Display all supermarket items

@app.get("/items")
def display_items():

    result = (
        {
            "item": items[i],
            "price": prices[i],
            "stock": stock[i]
        }
        for i in range(len(items))
    )

    return list(result)


# GET - Search supermarket item

@app.get("/items/{item_name}")
def search_item(item_name: str):

    if item_name in items:

        index = items.index(item_name)

        return {
            "item": items[index],
            "price": prices[index],
            "stock": stock[index]
        }

    return {"message": "Item not found!"}


# PUT - Update item price

@app.put("/items/{item_name}/price")
def update_price(item_name: str, new_price: float):

    if item_name in items:

        index = items.index(item_name)

        prices[index] = new_price

        return {
            "message": "Price updated successfully",
            "item": item_name,
            "new_price": new_price
        }

    return {"message": "Item not found!"}


# PUT - Update item stock

@app.put("/items/{item_name}/stock")
def update_stock(item_name: str, quantity: int):

    if item_name in items:

        index = items.index(item_name)

        stock[index] += quantity

        return {
            "message": "Stock updated successfully",
            "item": item_name,
            "stock": stock[index]
        }

    return {"message": "Item not found!"}


# DELETE - Delete supermarket item

@app.delete("/items/{item_name}")
def delete_item(item_name: str):

    if item_name in items:

        index = items.index(item_name)

        items.pop(index)
        prices.pop(index)
        stock.pop(index)

        return {
            "message": f"{item_name} deleted successfully!"
        }

    return {"message": "Item not found!"}