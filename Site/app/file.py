import os

from django.db.models import Q


def hardRemoveFile(id, File):
    for f in File.objects.filter(Q(id__in=id)):
        if f.file.path:
            try:
                os.remove(f.file.path)
            except Exception as e:
                print(e)
        f.delete()