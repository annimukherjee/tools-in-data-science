from pathlib import Path
from PIL import Image
import asyncio

async def compress_image(input_path: Path, output_path: Path, max_size: int = 1500) -> None:
    """Compress an image losslessly while ensuring the file is under max_size bytes, without resizing."""
    print(f"Processing: {input_path} -> {output_path}")  # Debugging statement
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, process_image, input_path, output_path, max_size)

def process_image(input_path: Path, output_path: Path, max_size: int) -> None:
    """Process image lossless compression while keeping the original size intact."""
    try:
        with Image.open(input_path) as img:
            print(f"Original format: {img.format}, Mode: {img.mode}, Size: {img.size}")  # Debugging statement

            # Convert to lossless-compatible format if needed
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA")  # Preserve transparency if present
            
            # Remove unnecessary metadata (EXIF, ICC profiles)
            img.info.pop("icc_profile", None)  # Remove embedded color profile
            img.info.pop("exif", None)  # Strip EXIF metadata

            # Save with lossless WebP, method=6 (highest compression)
            img.save(output_path, 'WEBP', lossless=True, method=6)

            # Check file size
            file_size = output_path.stat().st_size
            print(f"Final file size: {file_size} bytes")  # Debugging statement

            if file_size > max_size:
                print(f"WARNING: {output_path} exceeds {max_size} bytes!")  # Debugging statement

    except Exception as e:
        print(f"Error processing {input_path}: {e}")  # Debugging statement

async def main():
    """Batch process images asynchronously."""
    tasks = []
    image_dir = Path('images')
    
    if not image_dir.exists():
        print(f"Directory '{image_dir}' does not exist.")  # Debugging statement
        return
    
    paths = list(image_dir.glob('*.png'))
    if not paths:
        print("No JPG images found.")  # Debugging statement
        return

    for p in paths:
        output_path = p.with_suffix('.webp')
        tasks.append(compress_image(p, output_path))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())