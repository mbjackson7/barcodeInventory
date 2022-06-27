# Pantry Inventory Scanner
The purpose of the program is primarily to create a personal database of food items in your own pantry.

To use, this program must be connected to a personal database (I use Firestore as can be seen in the code).
This database will grow to contain all the products which the user typically buys, requiring less manual data entry.
When processing codes, they will be compared to the Nutritionix database when first encountered, and simply incremented otherwise.

The first way of using the program is to run scanner.py, which will contiously wait for codes, and process them on entry.
This should work with most standard USB laser barcode readers.

The second option is to run imageListener, which will use Google Cloud Vision API to identify text from a receipt, then
extract codes and process them. It is configured to listen for updates to a document on my personal database containing 
the data from an image uploaded from a webapp I have created for managing and viewing this database. 

This option is also currently configured to look for 9 digit codes specifically, as these are what appears on Target 
receipts, which are currently planned as the primary input for this program, as they neatly sort by department, including groceries.

One last note is that while the term "UPC" is used throughout the code, it is technically inaccurate since other codes may be used 
in the database and on barcodes in general. This was early in development when this project was more limited in scope, but simply 
serves as an easy shorthand now, and changing it to a more accurate term is low priority given that I am the sole developer on this 
project and am designing it for personal use.

That said, any numeric code can be used in this system provided that it will be a consistent representation of a given product that 
you intend to inventory.
