import sys

def count_jpegs(path):
    count = 0
    with open(path, "rb") as f:
        data = f.read()
        pos = 0
        while True:
            start = data.find(b"\xFF\xD8", pos)
            if start == -1:
                break
            end = data.find(b"\xFF\xD9", start)
            if end == -1:
                break
            count += 1
            pos = end + 2
    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python framecounter.py file.dat")
        sys.exit(1)
    afile = sys.argv[1]
    total = count_jpegs(afile)
    print(f"Frames found: {total}")

