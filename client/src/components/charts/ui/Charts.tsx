import * as echarts from "echarts";
import { FC, useEffect, useRef } from "react";

interface PropsWithChars {
  name_charts: string;
  type: "scatter" | "bar";
  xAxis: Array<string>;
  data: Array<number> | Array<[number, number]>;
}

export const Charts: FC<PropsWithChars> = ({
  name_charts,
  type,
  xAxis,
  data,
}) => {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!chartRef.current) return;

    const chart = echarts.init(chartRef.current);

    const options: echarts.EChartsOption = {
      title: {
        text: name_charts,
      },
      xAxis: {
        data: xAxis,
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          data: data,
          type: type,
        },
      ],
    };
    chart.setOption(options);

    return () => {
      chart.dispose();
    };
  }, [data, name_charts, type, xAxis]);

  return <div ref={chartRef} className="w-full h-[400px]"></div>;
};
