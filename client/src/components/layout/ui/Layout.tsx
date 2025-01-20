import { paths } from "@/config/nav";
import { Link, Outlet } from "react-router-dom";

export const Layout = () => {
  return (
    <>
      <header className="my-2 py-4 container mx-auto bg-gray-50 rounded">
        <nav className="flex flex-row gap-4 items-center justify-center">
          <Link to={paths.app.root.path}>Главная</Link>
          <Link to={paths.app.update.path}>Обновить файл</Link>
        </nav>
      </header>
      <Outlet />
    </>
  );
};
