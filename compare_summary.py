import json
from pathlib import Path
from llm_client import ask
from prompts import (
    V1_SYSTEM, V1_SUMMARY,
    V2_SYSTEM, V2_SUMMARY,
    V3_SYSTEM, V3_SUMMARY,
)

EXPERIMENT_NAME = "summary_variants"
INPUT_FILES = ["1.txt", "2.txt", "3.txt"]
INPUT_DIR = Path("examples")
OUTPUT_DIR = Path("examples/outputs") / EXPERIMENT_NAME

VARIANTS = [
    ("V1", V1_SYSTEM, V1_SUMMARY),
    ("V2", V2_SYSTEM, V2_SUMMARY),
    ("V3", V3_SYSTEM, V3_SUMMARY),
]

def run() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename in INPUT_FILES:
        input_path = INPUT_DIR / filename
        if not input_path.exists():
            print(f"Пропуск: {input_path} не найден")
            continue

        text = input_path.read_text(encoding="utf-8")
        stem = input_path.stem

        print(f"\n{'=' * 60}")
        print(f"ВХОД: {filename}")
        print(f"{'=' * 60}")

        for name, system, template in VARIANTS:
            user_prompt = template.format(text=text)
            result = ask(user_prompt, system=system)

            print(f"\n--- {name} ---")
            print(result)

            out_file = OUTPUT_DIR / f"{stem}__{name}.json"
            out_file.write_text(
                json.dumps(
                    {
                        "input_file": filename,
                        "variant": name,
                        "system": system,
                        "user_prompt": user_prompt,
                        "result": result,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

    print(f"\nВсе результаты сохранены в {OUTPUT_DIR}/")

if __name__ == "__main__":
    run()