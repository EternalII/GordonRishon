from django.contrib import admin
from .models import GuestEntry

@admin.register(GuestEntry)
class GuestEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date', 'approved', 'parent')
    list_filter = ('approved',)
    search_fields = ('name', 'subject', 'body')
    list_editable = ('approved',)
    actions = ['approve_entries', 'reject_entries', 'delete_entries']

    def approve_entries(self, request, queryset):
        queryset.update(approved=True)
    approve_entries.short_description = "Approve selected entries"

    def reject_entries(self, request, queryset):
        queryset.update(approved=False)
    reject_entries.short_description = "Reject selected entries"

    def delete_entries(self, request, queryset):
        queryset.delete()
    delete_entries.short_description = "Delete selected entries"