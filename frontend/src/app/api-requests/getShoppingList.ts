import axios from 'axios';
import { config } from '../Config';

export const getShoppingList = () => {
  return axios
    .get(`${config.urls.API_BASE_URL}api/planning/shoppinglist/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};
