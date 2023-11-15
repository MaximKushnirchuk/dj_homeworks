from django.contrib import admin

from .models import Article, Tag, Scope
from django import forms
from django.core.exceptions import ValidationError


class ArticleFormeSet(forms.BaseInlineFormSet):
    def clean(self):
        count = 0
        tags_list = []
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data["is_main"]:
                    count += 1
                if "tag_name" in form.cleaned_data:
                    if form.cleaned_data["tag_name"] not in tags_list:
                        tags_list.append(form.cleaned_data["tag_name"])
                    else:
                        raise ValidationError(
                            f"Тег {form.cleaned_data['tag_name']} указан больше одного раза !!!"
                        )
            else:
                print("empty dict() !!!!!!!!")
        if count == 0:
            raise ValidationError("Основной раздел не указан!")
        if count >= 2:
            raise ValidationError("Основной раздел может быть один!")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ArticleFormeSet


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "text", "published_at", "image"]
    inlines = [ScopeInline]


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
