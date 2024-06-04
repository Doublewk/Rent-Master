from django.db import models

class Leave_a_message(models.Model):
    username = models.CharField(max_length=256, verbose_name='用户名')
    content = models.TextField(verbose_name="内容")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")

    class Meta:
        db_table = "leave_a_message"
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "第{}条留言创建时期为{}".format(self.id, self.add_date)