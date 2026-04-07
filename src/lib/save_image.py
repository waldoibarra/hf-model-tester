from pathlib import Path

from PIL import Image

OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "assets/images"


def save_image(image: Image.Image, image_prefix: str = "example") -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = list(OUTPUT_DIR.glob(f"{image_prefix}-*.png"))
    next_index = len(existing) + 1
    output_path = OUTPUT_DIR / f"{image_prefix}-{next_index}.png"
    image.save(output_path)
    print(f"Saved image to {output_path}")
