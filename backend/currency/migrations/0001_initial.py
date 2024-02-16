from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_ictive", models.BooleanField(default=True)),
                (
                    "charcode",
                    models.CharField(
                        choices=[
                            ("AUD", "AUD"),
                            ("AZN", "AZN"),
                            ("GBP", "GBP"),
                            ("AMD", "AMD"),
                            ("BYN", "BYN"),
                            ("BGN", "BGN"),
                            ("BRL", "BRL"),
                            ("HUF", "HUF"),
                            ("VND", "VND"),
                            ("HKD", "HKD"),
                            ("GEL", "GEL"),
                            ("DKK", "DKK"),
                            ("AED", "AED"),
                            ("USD", "USD"),
                            ("EUR", "EUR"),
                            ("EGP", "EGP"),
                            ("INR", "INR"),
                            ("IDR", "IDR"),
                            ("KZT", "KZT"),
                            ("CAD", "CAD"),
                            ("QAR", "QAR"),
                            ("KGS", "KGS"),
                            ("CNY", "CNY"),
                            ("MDL", "MDL"),
                            ("NZD", "NZD"),
                            ("NOK", "NOK"),
                            ("PLN", "PLN"),
                            ("RON", "RON"),
                            ("XDR", "XDR"),
                            ("SGD", "SGD"),
                            ("TJS", "TJS"),
                            ("THB", "THB"),
                            ("TRY", "TRY"),
                            ("TMT", "TMT"),
                            ("UZS", "UZS"),
                            ("UAH", "UAH"),
                            ("CZK", "CZK"),
                            ("SEK", "SEK"),
                            ("CHF", "CHF"),
                            ("RSD", "RSD"),
                            ("ZAR", "ZAR"),
                            ("KRW", "KRW"),
                            ("JPY", "JPY"),
                        ],
                        max_length=3,
                        verbose_name="код валюты",
                    ),
                ),
                (
                    "rate",
                    models.DecimalField(
                        decimal_places=4,
                        max_digits=10,
                        verbose_name="значение",
                    ),
                ),
            ],
            options={
                "verbose_name": "валюта",
            },
        ),
    ]
