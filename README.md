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

The user can use their own custom CSV file inventory. To acheive this, there is a file in the repository called "data/default_products.csv"- copy this provided file into your local repository as "data/products.csv", where the program will be looking for it.

The program should prompt the user to input the identifier of each shopping cart item, one at a time.

If there are no products matching the given identifier, the program will validate by asking, "Hey, are you sure that product identifier is correct? Please try again!" At this point, the user can input a valid identifier.

When there are no more shopping cart items, the user should input the word `DONE` to indicate they are done with the process. 

After the user indicates there are no more items, the program will print a custom receipt on the screen.

### Game Simulation

User has choice to pass in name as environment variables through a ".env" in the project's root directory. A ".env" file is provided in the repository. Tax rate is the environment variable declared here, and the user can edit the ".env" file to adjust the tax rate.

Sample ".env" file contents:

```sh
# this is the ".env" file...
 
TAX_RATE=0.0875
```
### Run Program

Run the program with the following command.

```sh
python shopping_cart.py
```
