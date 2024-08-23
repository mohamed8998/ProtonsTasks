const prompt = require('prompt-sync')(); 
const fs = require('fs'); 

let groceryList = [];

function addItem() 
{ const item = prompt('Enter the grocery item: ');
    const price = parseFloat(prompt('Enter the price: '));
    groceryList.push({ item, price });
    console.log('Item added.'); }


function removeItem()
{ const item = prompt('Enter the grocery item to remove: ');
    groceryList = groceryList.filter(g => g.item !== item);
    console.log('Item removed.'); } 


function displayList()
{ console.log("Grocery List:");
    groceryList.forEach(g => console.log(`${g.item} - $${g.price}`)); }


function calculateTotal()
{ const total = groceryList.reduce((sum, g) => sum + g.price, 0); 
    console.log(`Total Cost: $${total}`); }


function saveToFile() 
{ fs.writeFileSync('groceryList.json', JSON.stringify(groceryList)); 
    console.log('List saved to groceryList.json'); } 

function loadFromFile()
{ if (fs.existsSync('groceryList.json'))
     { groceryList = JSON.parse(fs.readFileSync('groceryList.json', 'utf-8'));     
        console.log('List loaded from groceryList.json'); } 

        else { console.log('File not found.'); } }

    while (true) 
        { console.log("\n1. Add an item");
        console.log("2. Remove an item");
        console.log("3. Display the list"); 
        console.log("4. Calculate total");
        console.log("5. Save to file");
        console.log("6. Load from file"); 
        console.log("7. Exit"); 
        const choice = prompt('Enter your choice: '); 
        if (choice === '1') addItem(); 
        else if (choice === '2') removeItem(); 
        else if (choice === '3') 
        displayList(); 
            else if (choice === '4') 
            calculateTotal();
                else if (choice === '5')
                saveToFile(); 
                    else if (choice === '6')
                    loadFromFile(); 
                        else if (choice === '7')
                            break; 
                                 else console.log('Invalid choice.'); }