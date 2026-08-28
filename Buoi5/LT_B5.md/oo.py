import pandas as pd


def solution(df_receipt, df_store):
    print("=== P003: Hiển thị 10 bản ghi với các cột được chọn và đổi tên ===")
    p003_res = df_receipt[['sales_ymd', 'customer_id', 'product_cd', 'amount']].rename(
        columns={'sales_ymd': 'sales_date'}
    ).head(10)
    print(p003_res)
    print("\n" + "=" * 50 + "\n")

    print("=== P023: Tổng doanh thu (amount) và số lượng (quantity) theo cửa hàng ===")
    p023_res = df_receipt.groupby('store_cd')[['amount', 'quantity']].sum()
    print(p023_res)
    print("\n" + "=" * 50 + "\n")

    print("=== P033: Doanh thu trung bình theo cửa hàng (>= 330) ===")
    p033_res = df_receipt.groupby('store_cd')['amount'].mean()
    p033_res = p033_res[p033_res >= 330]
    print(p033_res)
    print("\n" + "=" * 50 + "\n")

    print("=== P034: Doanh thu trung bình theo khách hàng (loại bỏ ID bắt đầu bằng 'Z') ===")
    # Lọc bỏ khách hàng là nhân viên (customer_id bắt đầu bằng 'Z')
    df_filtered_cust = df_receipt[~df_receipt['customer_id'].astype(str).str.startswith('Z')]
    p034_res = df_filtered_cust.groupby('customer_id')['amount'].mean()
    print(p034_res)
    print("\n" + "=" * 50 + "\n")

    print("=== P036: Kết hợp df_receipt và df_store (10 bản ghi đầu tiên) ===")
    p036_res = pd.merge(df_receipt, df_store[['store_cd', 'store_name']], on='store_cd', how='inner').head(10)
    print(p036_res)

    return {
        "P003": p003_res,
        "P023": p023_res,
        "P033": p033_res,
        "P034": p034_res,
        "P036": p036_res
    }