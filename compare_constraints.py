import json
from pathlib import Path
from llm_client import ask
from prompts import (
    SUMMARY_PROMPT,
    SUMMARY_PROMPT_V_LIMITED,
)

EXPERIMENT_NAME = "constraints_experiment"
INPUT_FILES = ["1.txt", "2.txt", "3.txt"]
INPUT_DIR = Path("examples")
OUTPUT_DIR = Path("outputs") / EXPERIMENT_NAME

VARIANTS = [
    ("A_baseline",    None, SUMMARY_PROMPT),
    ("B_constrained", None, SUMMARY_PROMPT_V_LIMITED),
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