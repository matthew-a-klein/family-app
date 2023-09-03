import { createBrowserRouter } from 'react-router-dom';
import ShoppingListPage, {
  loader as shoppingListPageLoader,
} from './pages/ShoppingListPage';

export const Router = createBrowserRouter([
  {
    path: '/',
    element: <ShoppingListPage />,
    loader: shoppingListPageLoader,
  },
]);
