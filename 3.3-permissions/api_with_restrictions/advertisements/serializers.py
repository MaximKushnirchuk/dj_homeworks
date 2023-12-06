from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ("id", "title", "description", "creator", "status", "created_at")

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        print(" - - VALIDATE - - ")
        count_open_status = 0
        list_advertisement = Advertisement.objects.all()
        for adv in list_advertisement:
            if (
                adv.creator.id == self.context["request"].user.id
                and adv.status == "OPEN"
            ):
                count_open_status += 1
        print("Было насчитано ", count_open_status, "объявленийБ со статусом : OPEN")
        if self.context["request"].method == "POST":
            if count_open_status == 10:
                raise ValidationError(
                    "Нельзя иметь больше 10 объявлений со татусом : : OPEN"
                )
            print(
                "Количество объявдений со статусом OPEN теперь равно",
                count_open_status + 1,
            )

        elif self.context["request"].method == "PATCH":
            if (
                count_open_status == 10
                and self.context["request"].data["status"] == "OPEN"
            ):
                raise ValidationError(
                    "Нельзя иметь больше 10 объявлений со татусом: OPEN"
                )

        return data
