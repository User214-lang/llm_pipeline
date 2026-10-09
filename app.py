from pathlib import Path
from pipeline import process_text
import json
from pydantic import ValidationError

output_dir = Path("examples/outputs/pipeline_runs")
output_dir.mkdir(parents=True, exist_ok=True)

for path in sorted(Path("examples").glob("*.txt")):
    text = path.read_text(encoding="utf-8")

    try: 
        result = process_text(text)

    except json.JSONDecodeError:
        print(f"ERROR: {path.name}: модель вернула ответ, который не является JSON.")
        continue
    except ValidationError as e:
        print(f"ERROR: {path.name}: ответ модели не соответствует ожидаемой схеме.")
        print(f"Детали: {e}")
        continue

    print(f"=== {path.name} ===")
    print("\nSUMMARY:", result.summary)
    print("\nCATEGORY:", result.category)
    print("\nSENTIMENT:", result.sentiment)
    print("\nKEY POINTS:", result.key_points)
    print("\nFINAL:", result.final_answer)
    print()

    out_file = output_dir / f"{path.stem}.json"

    out_file.write_text(
    result.model_dump_json(indent=2, ensure_ascii=False),
    encoding="utf-8",
)
    
    print(f"Сохранено: {out_file}")