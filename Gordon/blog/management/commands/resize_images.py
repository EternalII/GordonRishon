from django.core.management.base import BaseCommand
from PIL import Image
import os
from django.conf import settings


class Command(BaseCommand):
    help = "Resize images to create low-res versions for responsive loading."

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='*', help='Image filenames to resize (leave empty to resize all)')
        parser.add_argument('--width', type=int, default=800, help='Max width for resized images')
        parser.add_argument('--quality', type=int, default=80, help='JPEG quality (1-100)')
        parser.add_argument('--create-all', action='store_true', help='Create low, medium, and high quality versions')

    def handle(self, *args, **options):
        Image.MAX_IMAGE_PIXELS = None

        static_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
        self.stdout.write(f"Looking in: {static_dir}")
        self.stdout.write(f"Files found: {os.listdir(static_dir)}")
        width = options['width']
        quality = options['quality']
        create_all = options['create_all']
        filenames = options['filenames']

        # If no filenames provided, process all images
        if not filenames:
            filenames = [f for f in os.listdir(static_dir) if f.endswith(('.jpg', '.jpeg', '.png')) and not f.endswith(('_low.jpg', '_medium.jpg', '_high.jpg'))]

        for filename in filenames:
            filepath = os.path.join(static_dir, filename)

            if not os.path.exists(filepath):
                self.stdout.write(f"Skipped {filename} (not found)")
                continue

            img = Image.open(filepath)

            # Define quality levels
            quality_levels = {
                'low': 50,
                'medium': 75,
                'high': 90
            } if create_all else {'_low': quality}

            for suffix, q in quality_levels.items():
                resized_img = img.copy()
                
                # Resize if wider than target
                if resized_img.width > width:
                    ratio = width / resized_img.width
                    new_height = int(resized_img.height * ratio)
                    resized_img = resized_img.resize((width, new_height), Image.Resampling.LANCZOS)

                # Save version
                suffix_name = f"_{suffix}" if not suffix.startswith('_') else suffix
                low_res_path = os.path.join(static_dir, filename.replace('.jpg', f'{suffix_name}.jpg').replace('.jpeg', f'{suffix_name}.jpg').replace('.png', f'{suffix_name}.png'))
                resized_img.save(low_res_path, quality=q, optimize=True)

                self.stdout.write(f"Resized {filename} to {low_res_path} (quality={q})")

        self.stdout.write("Image resizing complete.")