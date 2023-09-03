import { ActionFunctionArgs, useLoaderData } from 'react-router-dom';
import { getShoppingList } from '../api-requests/getShoppingList';
import { getTodoList } from '../api-requests/getTodoList';

export const loader = async (args: ActionFunctionArgs) => {
  const [shoppinglist, todolist] = await Promise.all([
    getShoppingList(),
    getTodoList(),
  ]);

  return shoppinglist && todolist ? [shoppinglist, todolist] : null;
};

export type ListItem = {
  name: string;
};

const ShoppingListPage = () => {
  const [shoppinglist, todolist] = useLoaderData() as [ListItem[], ListItem[]];
  return (
    <div className="max-w-lg mx-auto text-center ">
      <div className="text-3xl underline italic mt-4">Shopping List</div>
      {shoppinglist.map((listItem) => {
        return <div className="my-4">{listItem.name}</div>;
      })}
      <div>
        <div className="text-3xl underline italic mt-4">Todo List</div>
        {todolist.map((listItem) => {
          return <div className="my-4">{listItem.name}</div>;
        })}
      </div>
    </div>
  );
};

export default ShoppingListPage;
