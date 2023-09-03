import axios from 'axios';
import { config } from '../Config';

export const getTodoList = () => {
  return axios
    .get(`${config.urls.API_BASE_URL}api/planning/todolist/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};
