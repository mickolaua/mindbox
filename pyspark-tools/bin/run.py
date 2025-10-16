from pyspark_tools.dataset import create_test_datasets
from pyspark_tools.method import get_product_name_category_name_table
from pyspark.sql import SparkSession


def main():
    # Create session
    spark = SparkSession.builder.appName("ProductApp").getOrCreate()

    # Here we may think about how to get data, but for simplicity just create
    # test data
    df_products, df_categories, df_product_categories = create_test_datasets(
        spark)
    df_products.show()
    df_categories.show()
    df_product_categories.show()

    df_prod_cat_names = get_product_name_category_name_table(
        df_products, df_categories, df_product_categories)

    # Here we also may think on what to do with the table: display it, may be
    # save or upload somewhere
    df_prod_cat_names.orderBy(df_products["product_name"]).show()


if __name__ == "__main__":
    main()
