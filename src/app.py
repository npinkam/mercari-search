import mercari

def main():
    """
    Main function that searches for a specific item on Mercari and prints the product name and URL.

    Returns:
        None
    """
    keywords = "ファイナルファンタジー XII ザ ゾディアック エイジ"
    exclude_keywords = "ポスター"
    search_results = mercari.search(keywords=keywords, exclude_keywords=exclude_keywords,
                                    sort=mercari.MercariSort.SORT_PRICE, order=mercari.MercariOrder.ORDER_ASC)
    price_range_ = [1200, 1500]
    search_results = [item for item in search_results if price_range_[0] <= int(item.price) <= price_range_[1]]
    for item in search_results:
        print(f"Product: {item.productName} Price: {item.price} URL: {item.productURL}")


if __name__ == "__main__":
    main()
