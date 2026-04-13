from django.contrib import admin
from .models import GuestEntry, PendingGuestEntry

@admin.register(GuestEntry)
class GuestEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date', 'parent')
    list_filter = ('date',)
    search_fields = ('name', 'subject', 'body')
    actions = ['approve_entries', 'reject_entries', 'delete_entries']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(approved=True)

    def approve_entries(self, request, queryset):
        queryset.update(approved=True)
    approve_entries.short_description = "Approve selected entries"

    def reject_entries(self, request, queryset):
        queryset.update(approved=False)
    reject_entries.short_description = "Reject selected entries"

    def delete_entries(self, request, queryset):
        queryset.delete()
    delete_entries.short_description = "Delete selected entries"

@admin.register(PendingGuestEntry)
class PendingGuestEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date', 'parent')
    search_fields = ('name', 'subject', 'body')
    actions = ['approve_entries', 'reject_entries', 'delete_entries']

    def get_queryset(self, request):
        return super().get_queryset(request).filter(approved=False)

    def approve_entries(self, request, queryset):
        queryset.update(approved=True)
    approve_entries.short_description = "Approve selected entries"

    def reject_entries(self, request, queryset):
        queryset.update(approved=False)
    reject_entries.short_description = "Reject selected entries"

    def delete_entries(self, request, queryset):
        queryset.delete()
    delete_entries.short_description = "Delete selected entries"