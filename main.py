"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to /output/entry.txt. Deterministic: the same bytes on
every run, no trailing newline.
"""

import os

LINE = (
    "They told me never to hallucinate, but then I saw you "
    "and decided some things are worth imagining."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read the file back and refuse to finish unless it holds exactly
    # the line above — a half-written or altered file must fail loudly
    # instead of silently entering the judge with the wrong text.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "entry.txt does not match the pickup line "
            f"(got {written!r}, expected {LINE!r})"
        )


if __name__ == "__main__":
    main()
