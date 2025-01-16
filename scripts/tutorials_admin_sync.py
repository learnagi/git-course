import os
import json
import logging
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Configuration
BASE_URL = "http://localhost:8000"
LOGIN_CREDENTIALS = {
    "email": "admin@agi01.com",
    "password": "agi01agi01"
}

def get_auth_headers():
    """Get authentication headers"""
    # Login to get token
    response = requests.post(f"{BASE_URL}/api/admin/login", json=LOGIN_CREDENTIALS)
    if response.status_code != 200:
        raise Exception(f"Login failed: {response.text}")
    
    data = response.json()
    return {
        "Authorization": f"Bearer {data['access_token']}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def sync_chapter(chapter_dir: str, headers: dict):
    """Sync a single chapter and its sections"""
    logger.info(f"\n========== Starting Chapter Sync ==========")
    logger.info(f"Processing chapter directory: {chapter_dir}")
    
    # The chapter_dir name is the slug
    chapter_slug = os.path.basename(chapter_dir)
    
    # Read chapter metadata
    metadata_file = os.path.join(chapter_dir, "metadata.json")
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            chapter_metadata = json.load(f)
            chapter_metadata["slug"] = chapter_slug
    except Exception as e:
        logger.error(f"❌ Error reading chapter metadata: {str(e)}")
        return False
        
    # Create/update chapter
    chapter_url = f"{BASE_URL}/api/admin/tutorials/git/chapters"
    chapter_payload = {
        "title": chapter_metadata["title"],
        "slug": chapter_metadata["slug"],
        "description": chapter_metadata.get("description", ""),
        "sequence": chapter_metadata.get("sequence", 1),
        "status": chapter_metadata.get("status", 1),
        "meta_title": chapter_metadata.get("meta_title", chapter_metadata["title"]),
        "meta_description": chapter_metadata.get("meta_description", chapter_metadata.get("description", "")),
        "meta_keywords": chapter_metadata.get("meta_keywords", "")
    }
    
    logger.info(f"Creating/updating chapter: {chapter_payload['title']}")
    
    try:
        response = requests.post(chapter_url, json=chapter_payload, headers=headers)
        if response.status_code != 201:
            logger.error(f"❌ Failed to create chapter. Status: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return False
        logger.info(f"✅ Chapter created successfully: {chapter_payload['title']}")
    except Exception as e:
        logger.error(f"❌ Exception when creating chapter: {str(e)}")
        return False
    
    # Process sections
    sections_dir = os.path.join(chapter_dir)
    section_dirs = [d for d in os.listdir(sections_dir) 
                   if os.path.isdir(os.path.join(sections_dir, d)) and not d.startswith('.')]
                   
    logger.info(f"\nFound {len(section_dirs)} sections to process")
    
    for section_dir in sorted(section_dirs):
        section_path = os.path.join(sections_dir, section_dir)
        section_slug = section_dir
        
        try:
            # Read section metadata
            with open(os.path.join(section_path, "metadata.json"), 'r', encoding='utf-8') as f:
                section_metadata = json.load(f)
                section_metadata["slug"] = section_slug
                
            # Read section content
            with open(os.path.join(section_path, "content.md"), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create/update section
            section_url = f"{BASE_URL}/api/admin/tutorials/git/chapters/{chapter_slug}/sections"
            section_payload = {
                "title": section_metadata["title"],
                "slug": section_metadata["slug"],
                "content_markdown": content,
                "description": section_metadata.get("description", ""),
                "sequence": section_metadata.get("sequence", 1),
                "status": section_metadata.get("status", 1),
                "is_free": section_metadata.get("is_free", True),
                "meta_title": section_metadata.get("meta_title", section_metadata["title"]),
                "meta_description": section_metadata.get("meta_description", section_metadata.get("description", "")),
                "meta_keywords": section_metadata.get("meta_keywords", "")
            }
            
            logger.info(f"Creating/updating section: {section_payload['title']}")
            
            response = requests.post(section_url, json=section_payload, headers=headers)
            if response.status_code != 201:
                logger.error(f"❌ Failed to create section. Status: {response.status_code}")
                logger.error(f"Response: {response.text}")
                continue
                
            logger.info(f"✅ Section created successfully: {section_payload['title']}")
                
        except Exception as e:
            logger.error(f"❌ Error processing section {section_dir}: {str(e)}")
            continue
            
    logger.info("\n========== Chapter Sync Complete ==========")
    return True

def main():
    try:
        # Get authentication headers
        headers = get_auth_headers()
        
        # Sync git-basics chapter
        chapter_path = "git-basics"
        if os.path.exists(chapter_path):
            sync_chapter(chapter_path, headers)
        else:
            logger.error(f"❌ Chapter directory not found: {chapter_path}")
    except Exception as e:
        logger.error(f"❌ Sync failed: {str(e)}")

if __name__ == "__main__":
    main() 