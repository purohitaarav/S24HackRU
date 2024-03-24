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
