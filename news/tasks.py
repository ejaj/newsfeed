from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from newsupdateApi.sources import update_sources
from newsupdateApi.newsApi import update_news
from .notification import send_news_notification_to_user, delete_notification_news

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute=0, hour='6,18')),
    name="task_save_source_information",
    ignore_result=True
)
def task_save_source_information():
    """
    Save source of news and task run every 6pm and 6am daily.
    :return:
    """
    update_sources()
    logger.info("source information has been saved or updated")


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_save_news",
    ignore_result=True
)
def task_save_news():
    """
    Save update news and task run every 15 mins.
    :return:
    """
    update_news()
    logger.info("news information has been saved or updated")


@periodic_task(
    run_every=(crontab(minute='*/20')),
    name="task_send_news_notification_to_user",
    ignore_result=True
)
def task_send_news_notification_to_user():
    """
    Send email to user, task run every 20 mins.
    :return:
    """
    send_news_notification_to_user()
    logger.info("new news sent to user")


@periodic_task(
    run_every=(crontab(minute=0, hour=0)),
    name="task_delete_notification_news",
    ignore_result=True
)
def task_delete_notification_news():
    """
    delete notification news, run this task every midnight.
    :return:
    """
    delete_notification_news()
    logger.info("delete news notification information")
