from django.db import models
# Create model for contact page here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100,default="")
    user_phone = models.CharField(max_length=70,default="")
    message_content = models.TextField()
    time_tamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return 'Message from '+self.user_name + ' ' + self.user_email

         