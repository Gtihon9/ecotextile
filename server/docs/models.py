from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to="docs")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_link(self) -> str:
        return "/documents/" + str(self.pk)
