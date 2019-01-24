# coding=utf-8
from datetime import datetime, timezone
from framework.constant import DateTimeConst


class DateTimeUtils:

    @staticmethod
    def get_datetime_string(exp_format):
        return datetime.now().strftime(exp_format)

    @staticmethod
    def get_current_time(offset_from_utc=DateTimeConst.CURRENT_TIME_FROM_UTC,
                         date_time_format=DateTimeConst.HOUR_MIN_FORMAT):
        utc_dt = datetime.now(timezone.utc)
        dt = utc_dt.replace(hour=utc_dt.time().hour + offset_from_utc)
        return dt.strftime(date_time_format)
