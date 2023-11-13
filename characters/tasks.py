from celery import shared_task
from characters.scraper import async_characters_with_api


@shared_task
def run_sync_with_api() -> None:
    async_characters_with_api()
