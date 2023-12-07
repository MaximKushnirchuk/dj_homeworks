from rest_framework import serializers

from logistic.models import Stock, StockProduct, Product


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ["product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # products = ProductSerializer(read_only= True)
    class Meta:
        model = Stock
        fields = [
            "id",
            "address",
            "positions",
        ]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = super().create(validated_data)
        for position in positions:
            StockProduct(stock=stock, **position).save()
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop("positions")
        stock = super().update(instance, validated_data)
        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position["product"],
                defaults={"quantity": position["quantity"], "price": position["price"]},
            )
        return stock
