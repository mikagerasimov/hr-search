import { paths } from "@/config/nav";
import { Layout } from "@/components/layout";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const createAppRouter = () =>
  createBrowserRouter([
    {
      path: paths.app.root.path,
      element: <Layout />,
      children: [
        {
          path: paths.app.root.path,
          lazy: async () => {
            const m = await import("./routes/landing");
            return { element: <m.default /> };
          },
        },
        {
          path: paths.app.update.path,
          lazy: async () => {
            const m = await import("./routes/update");
            return { element: <m.default /> };
          },
        },
      ],
    },
  ]);

export const AppRouter = () => {
  const router = createAppRouter();

  return <RouterProvider router={router} />;
};
