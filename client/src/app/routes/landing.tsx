import { Charts } from "@/components/charts/ui/Charts";
import { Container } from "@/components/containers";

const Landing = () => {
  return (
    <Container variant={"default"}>
      <h1 className="font-medium text-2xl">Дашборды</h1>

      <div className="flex flex-col gap-4">
        <Charts
          name_charts="test"
          type={"scatter"}
          data={[120, 200, 150, 80, 70, 110, 130]}
          xAxis={["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]}
        />

        <Charts
          name_charts="test"
          type={"bar"}
          data={[120, 200, 150, 80, 70, 110, 130]}
          xAxis={["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]}
        />
      </div>
    </Container>
  );
};

export default Landing;
