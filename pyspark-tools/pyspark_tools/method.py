from pyspark.sql import DataFrame

__all__ = ["get_product_name_category_name_table"]


def get_product_name_category_name_table(
        df_products: DataFrame, df_categories: DataFrame,
        df_product_categories: DataFrame) -> DataFrame:
    return df_products.join(
        df_product_categories,
        on=df_products["product_id"] == df_product_categories["product_id"],
        how="leftouter").join(df_categories,
                              on=df_product_categories["category_id"] ==
                              df_categories["category_id"],
                              how="leftouter").select(
                                  df_products["product_name"],
                                  df_categories["category_name"])
