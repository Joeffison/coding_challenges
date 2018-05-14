export function books(state = [], action) {
  switch (action.type) {
    case 'ADD_BOOK':
      return [...state, action.payload];
    case 'REMOVE_BOOK':
      return state.filter(item => item.id !== action.payload.id);
    case 'TOGGLE_COMPLETE':
      return state.map(item => {
        if (item.id === action.payload.id) {
          return Object.assign({}, item, {
            complete: !item.complete
          });
        }
        return item;
      });
    case 'RATE':
      return state.map(item => {
        if (item.id === action.payload.id) {
          return Object.assign({}, item, {
            rating: action.payload.rating
          });
        }
        return item;
      });
    default:
      return state;
  }
}
