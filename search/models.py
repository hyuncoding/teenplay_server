from django.db import models

from member.models import Member
from teenplay_server.period import Period


class RecentSearch(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    keyword = models.TextField(null=False, blank=False)
    # 0: 삭제
    status = models.BooleanField(null=False, blank=False, default=1)

    class Meta:
        db_table = 'tbl_recent_search'



