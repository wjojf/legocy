from django.core.files.storage import default_storage
from django.db.models import FileField, ImageField
import os 


def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.
    Usage:
    >>> from django.db.models.signals import post_delete
    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in [f.name for f in sender._meta.get_fields()]:
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None

    if field and (isinstance(field, FileField) or isinstance(field, ImageField)):
        inst = kwargs["instance"]
        f = getattr(inst, fieldname)
        m = inst.__class__._default_manager
        if (
            hasattr(f, "path")
            and os.path.exists(f.path)
            and not m.filter(
                **{"%s__exact" % fieldname: getattr(inst, fieldname)}
            ).exclude(pk=inst._get_pk_val())
        ):
            try:
                default_storage.delete(f.path)
            except:
                pass


def images_cleanup(sender, **kwargs):
    try:
        legoSetImages = kwargs['instance'].LegoSetImage__set.all()
    except Exception as e:
        return 
    
    for img_obj in legoSetImages:
        try:
            print(f'Deleting {img_obj}...')
            img_obj.delete()
        except Exception as e:
            print(f'Error deleting {img_obj} -> {e}')


