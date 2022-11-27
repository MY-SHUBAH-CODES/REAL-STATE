from django.db import models

class Addland(models.Model):
    land_pic1=models.ImageField(upload_to="land_images/")
    land_pic2=models.ImageField(upload_to="land_images/",default='')
    land_pic3=models.ImageField(upload_to="land_images/",default='')
    land_pic4=models.ImageField(upload_to="land_images/",default='')
    land_pic5=models.ImageField(upload_to="land_images/",default='')
    land_description=models.TextField(max_length=1500)



class Addplot(models.Model):
    plot_pic1=models.ImageField(upload_to="plot_images/")
    plot_pic2=models.ImageField(upload_to="plot_images/",default='')
    plot_pic3=models.ImageField(upload_to="plot_images/",default='')
    plot_pic4=models.ImageField(upload_to="plot_images/",default='')
    plot_pic5=models.ImageField(upload_to="plot_images/",default='')
    plot_description=models.TextField(max_length=1500)






