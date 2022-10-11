from django.contrib import admin

from Site.models import Status, Render, Table, Column, PatternColumn, PatternTable, LastUpdateConfig, ControlUser, File, \
    Phone, Place


class StatusPanel(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]


admin.site.register(Status, StatusPanel)


class RenderPanel(admin.ModelAdmin):
    list_display = [field.name for field in Render._meta.fields]


admin.site.register(Render, RenderPanel)


class TablePanel(admin.ModelAdmin):
    list_display = [field.name for field in Table._meta.fields]


admin.site.register(Table, TablePanel)


class ColumnPanel(admin.ModelAdmin):
    list_display = [field.name for field in Column._meta.fields]
    list_editable = ['viewOrder']


admin.site.register(Column, ColumnPanel)


class PatternTablePanelInline(admin.TabularInline):
    model = PatternColumn
    extra = 0


class PatternTablePanel(admin.ModelAdmin):
    list_display = [field.name for field in PatternTable._meta.fields]
    inlines = [PatternTablePanelInline]


admin.site.register(PatternTable, PatternTablePanel)


class LastUpdateConfigPanel(admin.ModelAdmin):
    list_display = [field.name for field in LastUpdateConfig._meta.fields]


admin.site.register(LastUpdateConfig, LastUpdateConfigPanel)


class ControlUserPanel(admin.ModelAdmin):
    list_display = [field.name for field in ControlUser._meta.fields]


admin.site.register(ControlUser, ControlUserPanel)


class FilePanel(admin.ModelAdmin):
    list_display = [field.name for field in File._meta.fields]


admin.site.register(File, FilePanel)


class PhonePanel(admin.ModelAdmin):
    list_display = [field.name for field in Phone._meta.fields]


admin.site.register(Phone, PhonePanel)


class PlacePanel(admin.ModelAdmin):
    list_display = [field.name for field in Place._meta.fields]


admin.site.register(Place, PlacePanel)
