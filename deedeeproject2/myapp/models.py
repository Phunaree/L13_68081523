from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        # แสดงทั้งชื่อและอายุตามเงื่อนไข Lab 10 หน้า 30
        return f"{self.name} - {self.age}"