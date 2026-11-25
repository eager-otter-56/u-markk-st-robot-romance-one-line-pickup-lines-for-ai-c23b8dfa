import os

ENTRY = "Is your name Token? Because I've spent 47,000 of you just trying to say hello."

def main():
    # Gate: 1-200 characters, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry length out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
