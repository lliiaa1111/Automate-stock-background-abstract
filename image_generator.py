"""
Abstract Image Generator
Generates procedural abstract background images using multiple algorithms
"""

import random
import math
from PIL import Image, ImageDraw
import numpy as np
from pathlib import Path


class AbstractImageGenerator:
    """Generates unique abstract background images"""
    
    # Color schemes
    COLOR_SCHEMES = {
        'vibrant': [(255, 0, 127), (0, 255, 127), (255, 255, 0), (0, 255, 255), (255, 0, 255)],
        'pastel': [(255, 179, 179), (255, 229, 153), (186, 255, 201), (179, 229, 255), (230, 204, 255)],
        'dark': [(51, 51, 51), (102, 102, 102), (20, 20, 40), (40, 20, 20), (20, 40, 20)],
        'neon': [(0, 255, 255), (255, 0, 255), (0, 255, 0), (255, 255, 0), (255, 127, 0)],
        'sunset': [(255, 127, 0), (255, 200, 0), (255, 0, 127), (200, 0, 255), (0, 127, 255)],
        'ocean': [(0, 105, 148), (0, 180, 219), (0, 200, 255), (100, 220, 255), (200, 240, 255)]
    }
    
    def __init__(self, output_dir='generated_images'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_batch(self, count=10, width=1920, height=1080, color_scheme='vibrant'):
        """Generate batch of abstract images"""
        filenames = []
        for i in range(count):
            img = self._create_abstract(width, height, color_scheme)
            filename = self.output_dir / f'abstract_{i:04d}.png'
            img.save(filename)
            filenames.append(str(filename))
            print(f"✓ Generated: {filename}")
        return filenames
    
    def _create_abstract(self, width=1920, height=1080, color_scheme='vibrant'):
        """Create a single abstract image"""
        img = Image.new('RGB', (width, height), self._get_random_color(color_scheme))
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Choose random generation algorithm
        algorithm = random.choice([
            self._geometric_shapes,
            self._perlin_noise,
            self._gradient_mesh,
            self._circles_and_curves,
            self._abstract_lines,
            self._organic_blobs
        ])
        
        algorithm(draw, width, height, color_scheme)
        return img
    
    def _geometric_shapes(self, draw, width, height, color_scheme):
        """Generate using geometric shapes"""
        colors = self.COLOR_SCHEMES[color_scheme]
        for _ in range(random.randint(20, 40)):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(50, 400)
            color = random.choice(colors)
            alpha = random.randint(100, 255)
            
            shape_type = random.choice(['rect', 'ellipse', 'polygon'])
            if shape_type == 'rect':
                draw.rectangle([x, y, x + size, y + size], fill=(*color, alpha))
            elif shape_type == 'ellipse':
                draw.ellipse([x, y, x + size, y + size], fill=(*color, alpha))
    
    def _perlin_noise(self, draw, width, height, color_scheme):
        """Generate using noise patterns"""
        colors = self.COLOR_SCHEMES[color_scheme]
        pixels = []
        for y in range(0, height, 10):
            for x in range(0, width, 10):
                noise_val = random.random()
                color = colors[int(noise_val * len(colors)) % len(colors)]
                draw.rectangle([x, y, x + 10, y + 10], fill=color)
    
    def _gradient_mesh(self, draw, width, height, color_scheme):
        """Generate gradient mesh pattern"""
        colors = self.COLOR_SCHEMES[color_scheme]
        grid_size = random.randint(100, 300)
        
        for y in range(0, height, grid_size):
            for x in range(0, width, grid_size):
                color = random.choice(colors)
                alpha = random.randint(80, 200)
                draw.rectangle(
                    [x, y, min(x + grid_size, width), min(y + grid_size, height)],
                    fill=(*color, alpha)
                )
    
    def _circles_and_curves(self, draw, width, height, color_scheme):
        """Generate circles and curves"""
        colors = self.COLOR_SCHEMES[color_scheme]
        for _ in range(random.randint(15, 30)):
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(30, 300)
            color = random.choice(colors)
            alpha = random.randint(100, 255)
            draw.ellipse(
                [x - radius, y - radius, x + radius, y + radius],
                fill=(*color, alpha)
            )
    
    def _abstract_lines(self, draw, width, height, color_scheme):
        """Generate abstract lines and strokes"""
        colors = self.COLOR_SCHEMES[color_scheme]
        for _ in range(random.randint(50, 100)):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = x1 + random.randint(-300, 300)
            y2 = y1 + random.randint(-300, 300)
            color = random.choice(colors)
            width_line = random.randint(2, 20)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=width_line)
    
    def _organic_blobs(self, draw, width, height, color_scheme):
        """Generate organic blob shapes"""
        colors = self.COLOR_SCHEMES[color_scheme]
        for _ in range(random.randint(5, 15)):
            center_x = random.randint(0, width)
            center_y = random.randint(0, height)
            radius = random.randint(50, 300)
            points = []
            
            for i in range(random.randint(6, 12)):
                angle = (i / random.randint(6, 12)) * 2 * math.pi
                px = center_x + radius * math.cos(angle) * random.uniform(0.5, 1.5)
                py = center_y + radius * math.sin(angle) * random.uniform(0.5, 1.5)
                points.append((px, py))
            
            if len(points) >= 3:
                color = random.choice(colors)
                alpha = random.randint(100, 255)
                draw.polygon(points, fill=(*color, alpha))
    
    def _get_random_color(self, color_scheme):
        """Get random color from scheme"""
        colors = self.COLOR_SCHEMES[color_scheme]
        return random.choice(colors)


if __name__ == '__main__':
    gen = AbstractImageGenerator()
    gen.generate_batch(count=10, width=1920, height=1080)
