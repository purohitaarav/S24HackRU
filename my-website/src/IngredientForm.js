import React, { useState } from 'react';

const IngredientForm = ({ onSubmit }) => {
  // State to store current ingredient input
  const [ingredient, setIngredient] = useState('');

  // Function to handle input change
  const handleChange = (e) => {
    setIngredient(e.target.value);
  };

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Call parent onSubmit function with the new ingredient
    onSubmit(ingredient.trim());
    // Clear input field
    setIngredient('');
  };

  return (
    <form onSubmit={handleSubmit} className="ingredient-form">
      <label htmlFor="ingredient">Enter an Ingredient:</label>
      <input
        type="text"
        id="ingredient"
        value={ingredient}
        onChange={handleChange}
        placeholder="E.g., eggs, milk, bread..."
        required
      />
      <button type="submit">Add Ingredient</button>
    </form>
  );
}

export default IngredientForm;
