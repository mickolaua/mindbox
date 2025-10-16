from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType
from pyspark.sql.functions import col
from decimal import Decimal


def create_test_datasets(spark: SparkSession):
    products_schema = StructType([
        StructField("product_id", IntegerType()),
        StructField("product_name", StringType()),
        StructField("product_price", DecimalType(10, 2)),
    ])
    products = [(1, "keyborad", Decimal(1300.99)), (2, "mac", Decimal(9999)),
                (3, "laptop_hp", Decimal(2000)),
                (4, "airpods", Decimal(299.99)), (5, "bread", Decimal(1.50)),
                (6, "milk", Decimal(2.50))]
    df_products = spark.createDataFrame(products, products_schema)

    categories_schema = StructType([
        StructField("category_id", IntegerType()),
        StructField("category_name", StringType()),
    ])
    categories = [(1, "electronics"), (2, "accessory"), (3, "computer"),
                  (4, "paper")]
    df_categories = spark.createDataFrame(categories, categories_schema)

    product_category = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 1), (3, 3), (4, 1),
                        (4, 2)]
    product_category_schema = StructType([
        StructField("product_id", IntegerType(), True),
        StructField("category_id", IntegerType(), True)
    ])
    df_product_categories = spark.createDataFrame(product_category,
                                                  product_category_schema)
    return df_products, df_categories, df_product_categories
