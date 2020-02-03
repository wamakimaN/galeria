from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length =30)
  description = models.CharField(max_length =200)

  @classmethod
  def all_categs(cls):
    categories = cls.objects.all()
  
    return categories

  def __str__(self):
        return self.name

  def save_category(self):
    self.save()
  
class Picture(models.Model):
  image = models.ImageField(upload_to = 'pictures/')
  pic_name = models.CharField(max_length =30)
  pic_desc =models.CharField(max_length =200)
  category = models.ForeignKey(Category)

  @classmethod
  def all_pics(cls):
    pics = cls.objects.all()
    return pics
  
  def __str__(self):
        return self.pic_name

  def save_pic(self):
    self.save()

@classmethod
def categ_news(cls,category):
  categories = cls.objects.filter(category = category)




