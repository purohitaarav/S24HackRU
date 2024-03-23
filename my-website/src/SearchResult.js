import React, { useEffect, useState } from 'react';

const SearchResult = ({ ingredients }) => {
  // State to store search result
  const [searchResult, setSearchResult] = useState([]);

  // Function to simulate search for cheapest option
  const searchCheapestOption = async () => {
    // Simulate API call or search algorithm
    // In real application, you would fetch data from server based on user's input
    const result = await fakeAPICall(ingredients);
    setSearchResult(result);
  };

  // Fake API call function (replace with actual API call)
  const fakeAPICall = async (ingredients) => {
    // Simulate some delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    // Simulate search result
    return ingredients.map(ingredient => ({
      name: ingredient,
      cheapestOption: `Store X - $${Math.random() * 10}`, // Replace with actual data
      nearestStore: 'Store X', // Replace with actual data
    }));
  };

  // Effect to trigger search when ingredients change
  useEffect(() => {
    if (ingredients.length > 0) {
      searchCheapestOption();
    }
  }, [ingredients]);

  return (
    <div className="search-result">
      <h2>Search Result:</h2>
      <ul>
        {searchResult.map((item, index) => (
          <li key={index}>
            <strong>{item.name}:</strong> {item.cheapestOption} at {item.nearestStore}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SearchResult;
