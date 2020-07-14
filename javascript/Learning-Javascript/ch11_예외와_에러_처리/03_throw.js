function billPay(amount, payee, account) {
  if (amount > account.balance)
    throw new Error("잔액이 부족합니다.")
  account.transfer(payee, amount)
}