import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";

import "../index.css";

export const App = () => {
  const [data, setData] = useState();

  useEffect(() => {
    const fetchGet = async () => {
      const response = await fetch("http://127.0.0.1:8000/").catch((error) =>
        console.log(error)
      );

      if (!response?.ok) {
        throw new Error(`HTTP error!: ${response?.status}`);
      }

      const newData = await response.json();
      console.log(newData);
      setData(newData);
    };

    fetchGet();
  }, []);

  console.log(data);
  console.log(`http://127.0.0.1:8000/`);

  return (
    <div>
      <p>{JSON.stringify(data)}</p>
      <Button>init project</Button>
    </div>
  );
};
