"""Run the 15 examples and verify their documented output."""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    expected = json.loads((ROOT / "examples/expected_outputs.json").read_text(encoding="utf-8"))
    actual_files = {path.name for path in (ROOT / "examples").glob("[0-9][0-9]_*.py")}
    if actual_files != set(expected) or len(expected) != 15:
        print("Example files and the 15 expected-output fixtures must match.", file=sys.stderr)
        return 1
    failed = 0
    for filename, output in expected.items():
        try:
            result = subprocess.run(
                [sys.executable, str(ROOT / "examples" / filename)],
                cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=10,
            )
        except subprocess.TimeoutExpired:
            print(f"FAIL {filename}: exceeded 10 seconds")
            failed += 1
            continue
        if result.returncode != 0 or result.stdout != output or result.stderr:
            failed += 1
            print(f"FAIL {filename}")
            print(f"Expected: {output!r}")
            print(f"Actual:   {result.stdout!r}")
            print(result.stderr)
        else:
            print(f"PASS {filename}")
    print(f"\n{len(expected) - failed}/{len(expected)} examples passed.")
    return int(failed > 0)


if __name__ == "__main__":
    raise SystemExit(main())
