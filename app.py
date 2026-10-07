from pathlib import Path
from pipeline import process_text
import json
output_dir = Path("examples/output")
output_dir.mkdir(exist_ok=True)

for path in sorted(Path("examples").glob("*.txt")):
    text = path.read_text(encoding="utf-8")
    result = process_text(text)

    print(f"=== {path.name} ===")
    print("SUMMARY:", result["summary"])
    print("KEY POINTS:", result["key_points"])
    print("RESPONSE:", result["response"])
    print()

    out_file = output_dir / f"{path.stem}.json"
    out_file.write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
    )
    
    print(f"Сохранено: {out_file}")