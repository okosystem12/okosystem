from django.contrib import admin
from django.contrib.auth.models import Group

from Site.models import Status, Render, Table, Column, PatternColumn, PatternTable, LastUpdateConfig, ControlUser, File, \
    Phone, Place, StatusStage, Social, Post, Video, Groups, Inf, Photos, VideoChecks, PhotosChecks, GroupsChecks, \
    PostsChecks, AllUsersVK, CorruptInfo, TokensForVkUpdate, TokenAdmin, PostCorrupt, VideoCorrupt, GroupsCorrupt, \
    PhotosCorrupt, InfCorrupt, Environments, CorruptExtend, CorruptExtendFin

admin.site.unregister(Group)


class TokensForVkUpdatePanel(admin.ModelAdmin):
    list_display = [field.name for field in TokensForVkUpdate._meta.fields]


admin.site.register(TokensForVkUpdate, TokensForVkUpdatePanel)


class TokenAdminPanel(admin.ModelAdmin):
    list_display = [field.name for field in TokenAdmin._meta.fields]


admin.site.register(TokenAdmin, TokenAdminPanel)


class EnvironmentsPanel(admin.ModelAdmin):
    list_display = [field.name for field in Environments._meta.fields]


admin.site.register(Environments, EnvironmentsPanel)

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

class TabularInlineVC(admin.TabularInline):
    model = VideoCorrupt
    extra = 0


class VideoPanel(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.fields]
    inlines = [TabularInlineVC]


admin.site.register(Video, VideoPanel)


class TabularInlinePhC(admin.TabularInline):
    model = PhotosCorrupt
    extra = 0


class PhotosPanel(admin.ModelAdmin):
    list_display = [field.name for field in Photos._meta.fields]
    inlines = [TabularInlinePhC]


admin.site.register(Photos, PhotosPanel)


class TabularInlineGC(admin.TabularInline):
    model = GroupsCorrupt
    extra = 0


class GroupsPanel(admin.ModelAdmin):
    list_display = [field.name for field in Groups._meta.fields]
    inlines = [TabularInlineGC]


admin.site.register(Groups, GroupsPanel)


class TabularInlineIC(admin.TabularInline):
    model = InfCorrupt
    extra = 0


class InfPanel(admin.ModelAdmin):
    list_display = [field.name for field in Inf._meta.fields]
    inlines = [TabularInlineIC]


admin.site.register(Inf, InfPanel)


class TabularInlinePC(admin.TabularInline):
    model = PostCorrupt
    extra = 0


class PostPanel(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    inlines = [TabularInlinePC]


admin.site.register(Post, PostPanel)

class StatusStagePanel(admin.ModelAdmin):
    list_display = [field.name for field in StatusStage._meta.fields]


admin.site.register(StatusStage, StatusStagePanel)


class StatusPanel(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    list_filter = ["stage"]


admin.site.register(Status, StatusPanel)

class RenderPanel(admin.ModelAdmin):
    list_display = [field.name for field in Render._meta.fields]


admin.site.register(Render, RenderPanel)


class TablePanel(admin.ModelAdmin):
    list_display = [field.name for field in Table._meta.fields]


admin.site.register(Table, TablePanel)


class ColumnPanel(admin.ModelAdmin):
    list_display = [field.name for field in Column._meta.fields]
    list_filter = ["table"]
    search_fields = []


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



class CorruptInfoInline(admin.TabularInline):
    model = CorruptExtend
    extra = 0



class CorruptFinInfoInline(admin.TabularInline):
    model = CorruptExtendFin
    extra = 0


class CorruptInfoPanel(admin.ModelAdmin):
    list_display = [field.name for field in CorruptInfo._meta.fields]
    inlines = [CorruptFinInfoInline, CorruptInfoInline]


admin.site.register(CorruptInfo, CorruptInfoPanel)
