"""
Stock Image Uploader
Handles uploading images to multiple stock image platforms
"""

import requests
import logging
from pathlib import Path
from typing import List, Dict


class StockImageUploader:
    """Uploads images to stock image platforms"""
    
    def __init__(self, credentials: Dict):
        self.credentials = credentials
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
    
    def upload_batch(self, image_dir: str, platform: str, metadata: Dict = None) -> List[str]:
        """Upload batch of images to a platform"""
        if platform not in ['pixabay', 'unsplash', 'pexels']:
            self.logger.error(f"Unsupported platform: {platform}")
            return []
        
        image_dir = Path(image_dir)
        uploaded = []
        
        for image_path in sorted(image_dir.glob(f"{platform}_*.jpg")):
            try:
                result = self.upload_image(image_path, platform, metadata)
                if result:
                    uploaded.append(result)
                    self.logger.info(f"✓ Uploaded to {platform}: {image_path.name}")
            except Exception as e:
                self.logger.error(f"✗ Failed to upload {image_path.name}: {e}")
        
        return uploaded
    
    def upload_image(self, image_path: str, platform: str, metadata: Dict = None) -> str:
        """Upload a single image"""
        if platform == 'pixabay':
            return self._upload_pixabay(image_path, metadata)
        elif platform == 'unsplash':
            return self._upload_unsplash(image_path, metadata)
        elif platform == 'pexels':
            return self._upload_pexels(image_path, metadata)
    
    def _upload_pixabay(self, image_path: str, metadata: Dict = None) -> str:
        """Upload to Pixabay"""
        api_key = self.credentials.get('pixabay', {}).get('api_key')
        if not api_key:
            raise ValueError("Pixabay API key not configured")
        
        url = "https://pixabay.com/api/upload/"
        
        # Prepare metadata
        tags = metadata.get('tags', 'abstract, background, design') if metadata else 'abstract, background, design'
        title = metadata.get('title', Path(image_path).stem) if metadata else Path(image_path).stem
        description = metadata.get('description', 'Abstract background image') if metadata else 'Abstract background image'
        
        with open(image_path, 'rb') as f:
            files = {'image': f}
            data = {
                'key': api_key,
                'title': title,
                'tags': tags,
                'description': description,
                'type': 'photo'
            }
            
            response = self.session.post(url, files=files, data=data)
            response.raise_for_status()
            
            result = response.json()
            return result.get('id', image_path)
    
    def _upload_unsplash(self, image_path: str, metadata: Dict = None) -> str:
        """Upload to Unsplash"""
        access_token = self.credentials.get('unsplash', {}).get('access_token')
        if not access_token:
            raise ValueError("Unsplash access token not configured")
        
        url = "https://api.unsplash.com/photos"
        
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        # Prepare metadata
        title = metadata.get('title', Path(image_path).stem) if metadata else Path(image_path).stem
        description = metadata.get('description', 'Abstract background') if metadata else 'Abstract background'
        tags = metadata.get('tags', 'abstract,background,design').split(',') if metadata else ['abstract', 'background', 'design']
        
        with open(image_path, 'rb') as f:
            files = {'photo': f}
            data = {
                'title': title,
                'description': description,
                'tags': ','.join(tags),
                'made_by': 'Abstract Generator'
            }
            
            response = self.session.post(url, files=files, data=data, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            return result.get('id', image_path)
    
    def _upload_pexels(self, image_path: str, metadata: Dict = None) -> str:
        """Upload to Pexels"""
        api_key = self.credentials.get('pexels', {}).get('api_key')
        if not api_key:
            raise ValueError("Pexels API key not configured")
        
        # Note: Pexels requires curator status for uploads
        # This is a placeholder implementation
        self.logger.warning("Pexels uploads require curator status. Visit pexels.com/join-us/curators/")
        
        return image_path
    
    def validate_credentials(self, platform: str) -> bool:
        """Validate that credentials are configured"""
        if platform == 'pixabay':
            return bool(self.credentials.get('pixabay', {}).get('api_key'))
        elif platform == 'unsplash':
            return bool(self.credentials.get('unsplash', {}).get('access_token'))
        elif platform == 'pexels':
            return bool(self.credentials.get('pexels', {}).get('api_key'))
        return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Test credentials
    test_creds = {
        'pixabay': {'api_key': 'your_key_here'},
        'unsplash': {'access_token': 'your_token_here'}
    }
    
    uploader = StockImageUploader(test_creds)
    print("✓ Uploader initialized")
