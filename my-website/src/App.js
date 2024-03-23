import React, { useState } from 'react';
import './App.css'; // Import CSS file for styling
import IngredientForm from './IngredientForm'; // Import component for ingredient input form
import SearchResult from './SearchResult'; // Import component for displaying search result

const App = () => {
  // State to store user's input ingredients
  const [ingredients, setIngredients] = useState([]);

  // Function to handle submission of ingredient form
  const handleSubmit = (newIngredient) => {
    // Add new ingredient to the list
    setIngredients([...ingredients, newIngredient]);
  };

  return (
    <div className="app-container">
      <div className="rutgers-logo">R</div>
      <h1>Rutgers Grocery Helper</h1>
      <p className="tagline">Your One-Stop Shop for Smart Shopping</p>
      {/* Ingredient input form */}
      <IngredientForm onSubmit={handleSubmit} />
      {/* Display search result */}
      <SearchResult ingredients={ingredients} />
    </div>
  );
}

export default App;
