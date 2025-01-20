import { FC, PropsWithChildren, Suspense } from "react";

export const AppProvider: FC<PropsWithChildren> = ({ children }) => {
  return <Suspense fallback={<div>Загрузка...</div>}>{children}</Suspense>;
};
