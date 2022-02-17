# shopping-cart

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Setup

Clone this repository onto your local computer. Then navigate to wherever you downloaded the repo.

Create a virtual environment:

```sh
conda create -n shopping-env python=3.8
```

Activate the virtual environment:

```sh
conda activate shopping-env
```

Install package dependencies within the virtual environment:

```sh
pip install -r requirements.txt
```

## Usage Overview

The program asks the user (a checkout clerk) to input one or more product identifiers, then looks up the prices for each, then prints an itemized customer receipt including the total amount owed.

Instead of using a hard-coded products variable, download or copy the contents of the provided "products.csv" file into your project directory in a new subdirectory called "data" (so the path to the CSV file should be "data/products.csv"). Then update your code to read the products from this CSV file.

Ideally we'll allow the user to use their own custom CSV file inventory. To acheive this, save a copy of the provided "products.csv" file in your repo as "data/default_products.csv" and provide instructions in the README telling someone to copy this provided file into their local repo as "data/products.csv", where the program will be looking for it.

The program should prompt the checkout clerk to input the identifier of each shopping cart item, one at a time.

When the clerk inputs a product identifier, the program should validate it, displaying a helpful message like "Hey, are you sure that product identifier is correct? Please try again!" if there are no products matching the given identifier.

At any time the clerk should be able to indicate there are no more shopping cart items by inputting the word `DONE` or otherwise indicating they are done with the process. Before asking for identifiers, the program should provide clear instructions to the user about how to use the "DONE" keyword.

After the clerk indicates there are no more items, the program should print a custom receipt on the screen. The receipt should include the following components:

  + A grocery store name of your choice
  + A grocery store phone number and/or website URL and/or address of choice
  + The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. `2020-02-07 03:54 PM`)
  + The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. `$3.50`, etc.)
  + The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. `$19.47`), calculated as the sum of their prices
  + The amount of tax owed (e.g. `$1.70`), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
  + The total amount owed, formatted as US dollars and cents (e.g. `$21.17`), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
  + A friendly message thanking the customer and/or encouraging the customer to shop again
