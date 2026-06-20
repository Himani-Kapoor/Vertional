from django.db import models
from django.conf import settings


# Create your models here.
class Watch(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	target = models.CharField(max_length=100, default='store')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'target')

	def __str__(self):
		return f"{self.user} watches {self.target}"
