import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import products from './product';
// import reviews from './reviews'
import { reviewsReducer } from './reviews'
import { cartReducer } from './cart'
import { bookingsReducer } from './booking';
import { searchReducer } from './search';
import { favoriteReducer } from './favorite'

const rootReducer = combineReducers({
  session,
  products,
  review: reviewsReducer,
  cartReducer,
  bookingsReducer,
  searchReducer,
  favoriteReducer
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
