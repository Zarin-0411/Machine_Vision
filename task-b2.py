
#!/usr/bin/env python3
import cv2
import datetime
import os

# -----------------------------
# Your labels
# -----------------------------
LABEL_CUBE = "Cube 50 mm"
LABEL_HEMI = "Semi-sphere D100 mm"
NAME       = "Zarin Prova"

# -----------------------------
# Load snapshot
# -----------------------------
def find_image():
    for fname in ["snapshot.png"]:
        if os.path.exists(fname):
            return fname
    return None

def main():
    image_path = find_image()
    if image_path is None:
        print("Error: Place snapshot.png in this folder.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image.")
        return

    h, w, ch = img.shape
    print(f"Image shape: {h} x {w}, Channels: {ch}")

    out = img.copy()

    # -----------------------------
    # Object 1: Cube Bounding Box (RED)
    # Using your exact coordinates
    # -----------------------------
    x1, y1 = 355, 27
    x2, y2 = 546, 217

    cv2.rectangle(out, (x1, y1), (x2, y2), (0, 0, 255), 3)  # RED
    cv2.putText(out, LABEL_CUBE, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # -----------------------------
    # Object 2: Semi-sphere (GREEN)
    # center = (961,626), radius = 174
    # -----------------------------
    hemi_cx = 961
    hemi_cy = 626
    hemi_r  = 174

    cv2.circle(out, (hemi_cx, hemi_cy), hemi_r, (0,255,0), 3)  # GREEN
    cv2.putText(out, LABEL_HEMI, (hemi_cx - 180, hemi_cy + hemi_r + 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    # -----------------------------
    # Header: Name + Date
    # -----------------------------
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    overlay = out.copy()
    cv2.rectangle(overlay, (0, 0), (w, 50), (0, 0, 0), -1)
    out = cv2.addWeighted(overlay, 0.4, out, 0.6, 0)
    cv2.putText(out, f"{NAME} - {date_str}", (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # -----------------------------
    # Save output
    # -----------------------------
    cv2.imwrite("annotated_snapshot.png", out)
    print("Saved annotated_snapshot.png")

if __name__ == "__main__":
    main()
