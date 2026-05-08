"""
Image Processor
Optimizes and processes images for different stock platforms
"""

from PIL import Image, ImageEnhance
from pathlib import Path
import logging


class ImageProcessor:
    """Processes and optimizes images for stock platforms"""
    
    # Platform-specific requirements
    PLATFORM_SPECS = {
        'pixabay': {
            'min_width': 1920,
            'min_height': 1080,
            'formats': ['jpg', 'png'],
            'quality': 90
        },
        'unsplash': {
            'min_width': 1920,
            'min_height': 1200,
            'formats': ['jpg'],
            'quality': 85
        },
        'pexels': {
            'min_width': 2560,
            'min_height': 1920,
            'formats': ['jpg'],
            'quality': 85
        }
    }
    
    def __init__(self, input_dir='generated_images', output_dir='processed_images'):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.logger = logging.getLogger(__name__)
    
    def process_batch(self, platform='pixabay', enhance=True):
        """Process all images for a specific platform"""
        specs = self.PLATFORM_SPECS.get(platform)
        if not specs:
            self.logger.error(f"Unknown platform: {platform}")
            return []
        
        processed_files = []
        for image_path in self.input_dir.glob('*.png'):
            try:
                processed = self.process_image(image_path, platform, enhance)
                processed_files.append(processed)
                self.logger.info(f"✓ Processed: {image_path.name} for {platform}")
            except Exception as e:
                self.logger.error(f"✗ Failed to process {image_path.name}: {e}")
        
        return processed_files
    
    def process_image(self, image_path, platform='pixabay', enhance=True):
        """Process a single image"""
        img = Image.open(image_path)
        
        # Resize if needed
        specs = self.PLATFORM_SPECS[platform]
        if img.width < specs['min_width'] or img.height < specs['min_height']:
            img = self._resize_with_aspect_ratio(img, specs['min_width'], specs['min_height'])
        
        # Enhance if requested
        if enhance:
            img = self._enhance_image(img)
        
        # Convert to specified format
        output_format = specs['formats'][0].upper()
        if output_format == 'JPG':
            output_format = 'JPEG'
        
        # Save processed image
        output_path = self.output_dir / f"{platform}_{image_path.stem}.{specs['formats'][0]}"
        img.save(output_path, format=output_format, quality=specs['quality'], optimize=True)
        
        return str(output_path)
    
    def _resize_with_aspect_ratio(self, img, target_width, target_height):
        """Resize image maintaining aspect ratio"""
        img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Create new image with target size and paste resized image
        new_img = Image.new('RGB', (target_width, target_height), 'white')
        offset = ((target_width - img.width) // 2, (target_height - img.height) // 2)
        new_img.paste(img, offset)
        
        return new_img
    
    def _enhance_image(self, img):
        """Enhance image quality"""
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2)
        
        # Enhance brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.05)
        
        # Enhance color
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.15)
        
        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.1)
        
        return img
    
    def optimize_for_web(self, image_path, max_size_kb=500):
        """Optimize image for web (reduce file size)"""
        img = Image.open(image_path)
        quality = 90
        
        while quality > 10:
            temp_path = Path(str(image_path).replace('.png', f'_q{quality}.jpg'))
            img.save(temp_path, format='JPEG', quality=quality, optimize=True)
            
            if temp_path.stat().st_size / 1024 <= max_size_kb:
                return temp_path
            
            quality -= 5
        
        return temp_path


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    processor = ImageProcessor()
    processor.process_batch(platform='pixabay')
