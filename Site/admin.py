from django.contrib import admin

from Site.models import Status, Render, Table, Column, PatternColumn, PatternTable, LastUpdateConfig, ControlUser, File, \
    Phone, Place, StatusStage, Social, Post, Video, Groups, Inf, Photos, VideoChecks, PhotosChecks, GroupsChecks, \
    PostsChecks, AllUsersVK


class AllUsersVKPanel(admin.ModelAdmin):
    list_display = [field.name for field in AllUsersVK._meta.fields]


admin.site.register(AllUsersVK, AllUsersVKPanel)


class VideoChecksPanel(admin.ModelAdmin):
    list_display = [field.name for field in VideoChecks._meta.fields]


admin.site.register(VideoChecks, VideoChecksPanel)


class PhotosChecksPanel(admin.ModelAdmin):
    list_display = [field.name for field in PhotosChecks._meta.fields]


admin.site.register(PhotosChecks, PhotosChecksPanel)


class GroupsChecksPanel(admin.ModelAdmin):
    list_display = [field.name for field in GroupsChecks._meta.fields]


admin.site.register(GroupsChecks, GroupsChecksPanel)


class PostsChecksPanel(admin.ModelAdmin):
    list_display = [field.name for field in PostsChecks._meta.fields]


admin.site.register(PostsChecks, PostsChecksPanel)


class VideoPanel(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.fields]


admin.site.register(Video, VideoPanel)


class PhotosPanel(admin.ModelAdmin):
    list_display = [field.name for field in Photos._meta.fields]


admin.site.register(Photos, PhotosPanel)


class GroupsPanel(admin.ModelAdmin):
    list_display = [field.name for field in Groups._meta.fields]


admin.site.register(Groups, GroupsPanel)


class InfPanel(admin.ModelAdmin):
    list_display = [field.name for field in Inf._meta.fields]


admin.site.register(Inf, InfPanel)


class PostPanel(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]


admin.site.register(Post, PostPanel)


class StatusStagePanel(admin.ModelAdmin):
    list_display = [field.name for field in StatusStage._meta.fields]


admin.site.register(StatusStage, StatusStagePanel)


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


class SocialPanel(admin.ModelAdmin):
    list_display = [field.name for field in Social._meta.fields]


admin.site.register(Social, SocialPanel)
