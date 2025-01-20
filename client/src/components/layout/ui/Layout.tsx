import { Outlet } from "react-router-dom";

export const Layout = () => {
  return (
    <>
      <header>
        <nav>Навигация</nav>
      </header>
      <Outlet />
    </>
  );
};
