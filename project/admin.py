from django.contrib.admin.sites import AdminSite
from django.contrib.comments.models import Comment
from django.contrib.comments.admin import CommentsAdmin

from libazpm.contrib.blogging.models import Blog, Entry, BlogLink
from libazpm.contrib.blogging.admin import BlogAdmin, EntryAdmin
from libazpm.contrib.socialize.models import Bookmark
from libazpm.contrib.socialize.admin import BookmarkAdmin

from libscampi.contrib.cms.communism import models as communism_models, admin as communism_admin
from libscampi.contrib.cms.renaissance import models as renaissance_models, admin as renaissance_admin


blogging_admin = AdminSite()

blogging_admin.register(Bookmark, BookmarkAdmin)

blogging_admin.register(Blog, BlogAdmin)
blogging_admin.register(Entry, EntryAdmin)
blogging_admin.register(BlogLink)
blogging_admin.register(Comment, CommentsAdmin)

# Admin for communism
blogging_admin.register(communism_models.Theme)
blogging_admin.register(communism_models.StyleSheet, communism_admin.GenericDOMElementAdmin)
blogging_admin.register(communism_models.Javascript, communism_admin.GenericDOMElementAdmin)
blogging_admin.register(communism_models.Realm, communism_admin.RealmAdmin)
blogging_admin.register(communism_models.RealmNotification, communism_admin.RealmNotificationAdmin)
blogging_admin.register(communism_models.Section, communism_admin.SectionAdmin)
blogging_admin.register(communism_models.Slice, communism_admin.SliceAdmin)
blogging_admin.register(communism_models.NamedBox, communism_admin.BoxAdmin)
blogging_admin.register(communism_models.Commune, communism_admin.CommuneAdmin)
blogging_admin.register(communism_models.Application, communism_admin.ApplicationAdmin)

# Admin for renaissance
blogging_admin.register(renaissance_models.Image, renaissance_admin.FileBasedMediaAdmin)
blogging_admin.register(renaissance_models.Video, renaissance_admin.FileBasedMediaAdmin)
blogging_admin.register(renaissance_models.Audio, renaissance_admin.FileBasedMediaAdmin)
blogging_admin.register(renaissance_models.Document, renaissance_admin.FileBasedMediaAdmin)
blogging_admin.register(renaissance_models.Object, renaissance_admin.FileBasedMediaAdmin)
blogging_admin.register(renaissance_models.External, renaissance_admin.ExternalAdmin)

blogging_admin.register(renaissance_models.ImagePlaylist, renaissance_admin.ImagePlaylistAdmin)
blogging_admin.register(renaissance_models.VideoPlaylist, renaissance_admin.VideoPlaylistAdmin)
blogging_admin.register(renaissance_models.AudioPlaylist, renaissance_admin.AudioPlaylistAdmin)
blogging_admin.register(renaissance_models.DocumentPlaylist, renaissance_admin.DocumentPlaylistAdmin)
blogging_admin.register(renaissance_models.ObjectPlaylist, renaissance_admin.ObjectPlaylistAdmin)

blogging_admin.register(renaissance_models.ImageType, renaissance_admin.DimensionalMediaTypeAdmin)
blogging_admin.register(renaissance_models.VideoType, renaissance_admin.DimensionalMediaTypeAdmin)
blogging_admin.register(renaissance_models.ObjectType, renaissance_admin.DimensionalMediaTypeAdmin)
blogging_admin.register(renaissance_models.AudioType, renaissance_admin.MediaTypeAdmin)
blogging_admin.register(renaissance_models.DocumentType, renaissance_admin.MediaTypeAdmin)

blogging_admin.register(renaissance_models.MediaInlineTemplate)
blogging_admin.register(renaissance_models.MediaPlaylistTemplate)