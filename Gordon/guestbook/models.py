from django.db import models
from django.utils import timezone

class GuestEntry(models.Model):
    name = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=20000)
    date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self):
        return f"{self.name or 'Anonymous'} — {self.subject or 'No subject'}"

    class Meta:
        ordering = ['-date']

class PendingGuestEntry(GuestEntry):
    class Meta:
        proxy = True
        verbose_name = "Pending Entry"
        verbose_name_plural = "Pending Entries"