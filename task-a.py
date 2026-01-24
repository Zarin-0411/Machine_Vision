import cv2
import matplotlib.pyplot as plt

img = cv2.imread("tiger.jpg")     
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
R, G, B = cv2.split(img_rgb)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# --- Original Image ---
axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title("Original Image (RGB)")
axes[0, 0].axis("off")

# --- Red Channel ---
axes[0, 1].imshow(R, cmap='gray')
axes[0, 1].set_title("RED channel")
axes[0, 1].axis("off")

# --- Green Channel ---
axes[1, 0].imshow(G, cmap='gray')
axes[1, 0].set_title("GREEN channel")
axes[1, 0].axis("off")

# --- Blue Channel ---
axes[1, 1].imshow(B, cmap='gray')
axes[1, 1].set_title("BLUE channel")
axes[1, 1].axis("off")

plt.tight_layout()
plt.savefig("My_Tiger.png", dpi=300)
plt.show()

