from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100) #博客题目
    category = models.CharField(max_length = 50,blank = True) #博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期
    content = models.TextField(blank = True,null = True) #博客文章正文
    #python2使用__unicode__,python3使用__str__
    def __str__(self):
        return self.title
    """
    其中__str__(self) 函数Article对象要怎么表示自己,
    一般系统默认使用<Article: Article object> 来表示对象,
    通过这个函数可以告诉系统使用title字段来表示这个对象
    """
    class Meta: #按时间下降排序
        ordering = ['-date_time']
