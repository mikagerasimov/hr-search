import { cva, type VariantProps } from "class-variance-authority";
import { FC, ReactNode } from "react";

import { cn } from "@/lib/shadcn/utils";

const containerVariants = cva("", {
  variants: {
    variant: {
      default: "container mx-auto px-4",
      center: "h-screen flex flex-col items-center justify-center",
    },
  },
});

interface ContaierProps extends VariantProps<typeof containerVariants> {
  children: ReactNode;
}

export const Container: FC<ContaierProps> = ({ children, variant }) => {
  return <main className={cn(containerVariants({ variant }))}>{children}</main>;
};
