# 새로운 작성중
# 테스트  1 작업중이였음
# won 작업
# seung 작업
# 김태연 작업중
# 리베이스테스트
from django.contrib import admin, messages

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "created_at", "updated_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "content", "user__username", "user__nickname")
    readonly_fields = ("created_at", "updated_at")
    actions = ["reset_rendered_content"]

    def reset_rendered_content(self, request, queryset):
        for post in queryset:
            post.rendered_content = ""
            post.save(update_fields=["rendered_content"])

        count = queryset.count()
        messages.success(request, f"{count}개의 게시글 렌더링 내용이 초기화되었습니다.")

    reset_rendered_content.short_description = "선택된 게시글의 렌더링된 내용 초기화"
