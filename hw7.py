cart = {}

while True:
    print("[구입]")
    product_name = input("상품명? ")
    if not product_name:  # 상품명이 빈 문자열일 경우 루프 종료
        break
    quantity = int(input("수량은? "))
    cart[product_name] = quantity
    print(f"장바구니에{product_name} {quantity}개가 담겼습니다.")

print(f"장바구니 보기: {cart}")

print("[검색]")
product_name = input("장바구니에서 확인하고자하는 상품은? ")
if product_name in cart:
    print(f"{product_name}은(는) {cart[product_name]}개 담겨 있습니다.")
else:
    print(f"{product_name}은(는) 장바구니에 없습니다.")