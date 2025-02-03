from pathlib import Path
from PIL import Image
import io

def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if needed
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Create output directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Optimize for web
            img.save(output_path, 'WEBP', quality=quality, optimize=True)
    except (IOError, OSError) as e:
        raise Exception(f"Error processing {input_path}: {str(e)}")

def batch_process_images(input_dir: Path = Path('images')) -> None:
    """Process all PNG images in the given directory."""
    if not input_dir.exists():
        raise FileNotFoundError(f"Directory not found: {input_dir}")
        
    paths = input_dir.glob('*.png')
    for p in paths:
        try:
            compress_image(p, p.with_suffix('.webp'))
            print(f"Successfully compressed: {p}")
        except Exception as e:
            print(f"Failed to process {p}: {str(e)}")

# Usage
if __name__ == "__main__":
    batch_process_images()