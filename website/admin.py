from django.contrib import admin

from website.models import Website, Snap


class SnapInline(admin.StackedInline):
    model = Snap


class SnapAdmin(admin.ModelAdmin):
    list_display = ("filename", "website", "id", )

    def filename(self, obj):
        return obj.get_filename()

    filename.short_description = "ファイル名"

    def associated_website(self, obj):
        website = obj.website
        title = website.title
        return title

    associated_website.short_description = "ウェブサイト名"


admin.site.register(Snap, SnapAdmin)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("title", "url", )
    readonly_fields = ("timestamp", "updated", )
    inlines = (SnapInline, )


admin.site.register(Website, WebsiteAdmin)
