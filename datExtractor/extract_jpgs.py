import sys, os

def extract_jpgs(dat_path, out_dir, max_frames=5):
    with open(dat_path, "rb") as f:
        data = f.read()

    # Search for sequences FF D8 ... FF D9
    start = 0
    count = 0
    while True:
        soi = data.find(b"\xFF\xD8", start)
        if soi == -1:
            break
        eoi = data.find(b"\xFF\xD9", soi)
        if eoi == -1:
            break
        frame = data[soi:eoi+2]
        out_path = os.path.join(out_dir, f"frame_{count:04d}.jpg")
        with open(out_path, "wb") as out:
            out.write(frame)
        print(f"Extracted {out_path} ({len(frame)} bytes)")
        count += 1
        if count >= max_frames:
            break
        start = eoi+2

    print(f"Total frames extracted: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use: python extract_jpgs.py file.dat output_folder [max_frames]")
        sys.exit(1)
    dat = sys.argv[1]
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    maxf = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    extract_jpgs(dat, outdir, maxf)