from django.contrib import admin
from .models import post
from .models import user_comment
from .models import edit_profile
from .models import chat
from .models import doctor

admin.site.register (post)
admin.site.register (user_comment)
admin.site.register (edit_profile)
admin.site.register (chat)
admin.site.register (doctor)
