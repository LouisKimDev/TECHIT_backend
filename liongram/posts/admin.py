from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'image',
                    'content',
                    'created_at',
                    'view_count',
                    'writer')
    # list_editable('content', )
    list_filter = ['created_at']
    search_fields = ['content', 'writer__username']
    readonly_fields = ('created_at',)
    inlines = [CommentInline]

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.update(status='게시글 삭제 됨')
        queryset.update(status='p')

# admin.site.register(Comment)