# epam-python-test
This is a Python project containing three applications: Dictionary, Shopping, and N-letters. To use any of them, you need to navigate to the respective folder and follow these steps:

- To create a Docker image: docker build -t {image-name} .
- To run the application in interactive mode: docker run -it {image-name}
- To use the application, follow the instructions displayed when the application starts.

The interactive mode of Docker allows you to access all the application's features.


# Dictionary
This application works as a dictionary. You can:

- Add words with their meanings.
- Search for a specific word to view its meaning.
- List all the words saved in the dictionary.

# Shopping
This application functions as an online supermarket. The main goal is to specify which items you'd like to buy and calculate the total cost based on their prices and applicable taxes. The application:

- Comes pre-configured with a list of supermarket items and a default tax rate.
- Allows you to add new items with their prices.
- Lets you modify the tax rate.
- Enables you to retrieve the price of an item.
- Provides the total cost, including taxes, for selected items.

#N-Letters
This is a simple application that contains an array of words. You can construct a word by taking the letter at the corresponding position from each word in the array.
For example, given the words ['yoda', 'best', 'has'], you will construct the word 'yes'.

# Important Notes
Remember to follow the instruction of each application.
