print(sum(0.1 for i in range(10)) == 1.0)  # 부정확하지

# 정확한 10진법 부동 소수점 숫자가 필요하다면 !
from decimal import Decimal

print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
