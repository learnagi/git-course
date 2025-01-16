import logging
from tutorials_admin_sync import TutorialsAdminSync
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_auth():
    """Test authentication and token caching"""
    syncer = TutorialsAdminSync(Path("."))
    
    # Test getting headers (this will trigger authentication)
    try:
        headers = syncer.get_headers()
        logger.info("Successfully got headers with token")
        logger.debug(f"Headers: {headers}")
    except Exception as e:
        logger.error(f"Failed to get headers: {e}")
        return False

    # Test API request
    try:
        response = syncer.api_request('GET', 'tutorials')
        logger.info("Successfully made API request")
        logger.debug(f"Response: {response}")
        return True
    except Exception as e:
        logger.error(f"Failed to make API request: {e}")
        return False

def test_tutorial_sync():
    """Test tutorial synchronization"""
    syncer = TutorialsAdminSync(Path("."))
    
    # Test tutorial sync with sample data
    tutorial_data = {
        "title": "Test Tutorial",
        "description": "This is a test tutorial",
        "keywords": ["test", "tutorial"],
        "slug": "test-tutorial",
        "status": 1,
        "type": 1,
        "level": 1
    }
    
    try:
        # 先尝试获取响应内容，看看具体的错误信息
        response = syncer.api_request('POST', 'tutorials', tutorial_data)
        logger.debug(f"Tutorial creation response: {response}")
        
        result = syncer.sync_tutorial(tutorial_data)
        logger.info(f"Tutorial sync result: {result}")
        return result
    except Exception as e:
        logger.error(f"Tutorial sync failed: {e}")
        return False

if __name__ == "__main__":
    logger.info("Starting tests...")
    
    # Test authentication
    logger.info("Testing authentication...")
    if test_auth():
        logger.info("Authentication test passed")
    else:
        logger.error("Authentication test failed")
        exit(1)
    
    # Test tutorial sync
    logger.info("Testing tutorial sync...")
    if test_tutorial_sync():
        logger.info("Tutorial sync test passed")
    else:
        logger.error("Tutorial sync test failed")
        exit(1)
    
    logger.info("All tests completed successfully") 