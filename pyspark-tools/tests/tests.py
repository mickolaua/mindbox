from pyspark_tools.method import get_product_name_category_name_table
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType
from pyspark.sql.functions import col
from decimal import Decimal
import pytest


def test_all_categories_for_all_products():
    spark = SparkSession.builder.appName("ProductApp").getOrCreate()
    products_schema = StructType([
        StructField("product_id", IntegerType()),
        StructField("product_name", StringType()),
        StructField("product_price", DecimalType(10, 2)),
    ])
    products = [(1, "keyborad", Decimal(1300.99)), (2, "mac", Decimal(9999)),
                (3, "laptop_hp", Decimal(2000)),
                (4, "airpods", Decimal(299.99))]
    df_products = spark.createDataFrame(products, products_schema)

    categories_schema = StructType([
        StructField("category_id", IntegerType()),
        StructField("category_name", StringType()),
    ])
    categories = [(1, "electronics"), (2, "accessory"), (3, "computer")]
    df_categories = spark.createDataFrame(categories, categories_schema)

    product_category = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 1), (3, 3)]
    product_category_schema = StructType([
        StructField("product_id", IntegerType(), True),
        StructField("category_id", IntegerType(), True)
    ])
    df_product_categories = spark.createDataFrame(product_category,
                                                  product_category_schema)
    df_prod_cat_names = get_product_name_category_name_table(
        df_products, df_categories, df_product_categories)

    correct_data = [("airpods", "accessory"), ("airpods", "electronics"),
                    ("keyborad", "accessory"), ("keyborad", "electronics"),
                    ("laptop_hp", "computer"), ("laptop_hp", "electronics"),
                    ("mac", "computer"), ("mac", "electronics")]
    correct_answer = spark.createDataFrame(correct_data,
                                           ["product_name", "category_name"])

    count_incorrect = correct_answer.join(
        df_prod_cat_names,
        on=df_prod_cat_names["product_name"] == correct_answer["product_name"],
        how="outer").select(col("category_name")).join(df_prod_cat_names,
                                                       on="category_name",
                                                       how="outer").count()

    assert count_incorrect == 0, "DataFrames are not equal"
