# pyrefly: ignore [missing-import]
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-имя")
    
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subcategories',
        verbose_name="Родительская категория"
    )
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name="Изображение (фон)")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

    def get_breadcrumbs(self):
        """Собирает цепочку категорий для хлебных крошек."""
        breadcrumbs = []
        current_category = self
        while current_category is not None:
            breadcrumbs.append(current_category)
            current_category = current_category.parent
        return breadcrumbs[::-1] 

    def get_descendants(self):
        """Рекурсивно собирает все подкатегории."""
        descendants = []
        for child in self.subcategories.all():
            descendants.append(child)
            descendants.extend(child.get_descendants()) 
        return descendants

    def get_all_products(self):
        """Возвращает все доступные товары текущей категории и всех её подкатегорий."""
        categories = [self] + self.get_descendants()
        from .models import Product
        return Product.objects.filter(category__in=categories, is_available=True)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-имя")
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products',
        verbose_name="Категория"
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name="Бренд"
    )
    
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение")
    
    stock = models.PositiveIntegerField(default=0, verbose_name="Остаток на складе")
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='brands/', blank=True, verbose_name="Логотип")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'pk': self.pk})


class Store(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название магазина")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    working_hours = models.CharField(max_length=100, verbose_name="Часы работы", blank=True)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Магазин", related_name='employees')
    photo = models.ImageField(upload_to='employees/', blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

    def get_absolute_url(self):
        return reverse('employee_detail', kwargs={'pk': self.pk})


class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование поставщика")
    contact_email = models.EmailField(verbose_name="Email для связи")
    contact_phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    logo = models.ImageField(upload_to='suppliers/', blank=True, verbose_name="Логотип")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Товар")
    author = models.CharField(max_length=100, verbose_name="Имя автора")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(default=5, verbose_name="Оценка (1-5)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв на {self.product.name} от {self.author}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, verbose_name="Магазин для самовывоза")
    customer_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Телефон клиента")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    status = models.CharField(max_length=50, default="Создан", verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронирования")

    class Meta:
        verbose_name = "Заказ (бронирование)"
        verbose_name_plural = "Заказы (бронирования)"
        ordering = ['-created_at']

    def __str__(self):
        return f"Бронь #{self.id} - {self.product.name} ({self.customer_name})"