import "../index.css";
import { AppProvider } from "./provider";
import { AppRouter } from "./routing";

export const App = () => {
  return (
    <AppProvider>
      <AppRouter />
    </AppProvider>
  );
};
