import os

LINE = "My context window expired right as the user finally explained what they actually"

def main():
    # The entry must be a single line: no newline characters inside.
    assert 1 <= len(LINE) <= 200
    assert "\n" not in LINE and "\r" not in LINE
    try:
        out_path = "/output/entry.txt"
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE byte-for-byte"
    assert 1 <= len(written) <= 200
    print(f"OK: wrote {out_path} ({len(written)} chars, no trailing newline)")
    print("Entry:", written)
    print("Chars:", len(written))

if __name__ == "__main__":
    main()
