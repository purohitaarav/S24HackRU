<<<<<<< Updated upstream
function getStoreDetails() {
    fetch('http://localhost:8002/store')
        .then(response => response.json())
        .then(data => {
            document.getElementById('storeResponse').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
}

function getItemDetails() {
    const recipe = document.getElementById('recipeInput').value;
    fetch(`http://localhost:8002/item?recipe=${recipe}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('itemResponse').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
}





=======
document.getElementById('recipeForm').addEventListener('submit', function(event) {
        event.preventDefault();
    
        const recipe = document.getElementById('recipe').value;
        fetchRecipe(recipe);
        fetchRecipeImage(recipe);
    });
    
    function fetchRecipe(recipeName) {
        fetch(`http://localhost:8002/item?recipe=${encodeURIComponent(recipeName)}`)
            .then(response => response.json())
            .then(data => {
                displayResult(data);
            });
    }
    
    function displayResult(data) {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';
    
        if (Object.keys(data).length === 0) {
            resultDiv.innerHTML = `<p>No items found for the given recipe.</p>`;
        } else {
            const table = document.createElement('table');
            table.classList.add('result-table');
    
            const headerRow = document.createElement('tr');
            table.appendChild(headerRow);
    
            const ingredientHeader = document.createElement('th');
            ingredientHeader.textContent = 'Ingredient';
            headerRow.appendChild(ingredientHeader);
    
            const priceHeader = document.createElement('th');
            priceHeader.textContent = 'Price';
            headerRow.appendChild(priceHeader);
    
            for (const [itemName, itemInfo] of Object.entries(data)) {
                const row = document.createElement('tr');
    
                const ingredientCell = document.createElement('td');
                ingredientCell.textContent = itemName;
                row.appendChild(ingredientCell);
    
                const priceCell = document.createElement('td');
                priceCell.textContent = `${itemInfo.Price}`;
                row.appendChild(priceCell);
    
                table.appendChild(row);
            }
    
            resultDiv.appendChild(table);
        }
    }
    
    function fetchRecipeImage(recipe) {
        const apiUrl = 'https://api.edamam.com/api/recipes/v2?type=public&beta=false&q=' + encodeURIComponent(recipe) + '&app_id=ac2cee73&app_key=813286124be5b0c3817b0fb7f8034476';
    
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.hits && data.hits.length > 0 && data.hits[0].recipe) {
                    const recipeImage = data.hits[0].recipe;
                    displayRecipeImage(recipeImage.image);
                } else {
                    displayRecipeImage('');
                }
            });
    }
    
    function displayRecipeImage(imageSrc) {
        const recipeImage = document.getElementById('recipe-image');
        recipeImage.innerHTML = '';
    
        if (imageSrc) {
            const img = document.createElement('img');
            img.src = imageSrc;
            img.alt = 'Recipe Picture';
    
            recipeImage.appendChild(img);
        } else {
            recipeImage.innerHTML = 'No Image Available';
        }
    }
>>>>>>> Stashed changes
