function solution(reqs) {
  let codes = [];
  let accounts = [];

  const isAccountExist = (accountId) => {
    return accounts.findIndex(account => account.id === accountId)
  };

  for (let req of reqs) {
    const [command, accountId, number] = req.split(' ');
    const accountIdx = isAccountExist(accountId);
    if (command === "CREATE") {
      if (accountIdx !== -1) {
        // 계설된 계좌
        codes.push(403)
      } else {
        // 없으면
        accounts.push(
          {id: accountId, amount: 0, limit: -number},
        );
        codes.push(200)
      }
    } else if (command === "DEPOSIT") {
      if (accountIdx !== -1) {
        // 입금
        accounts[accountIdx].amount += parseInt(number);
        // 200
        codes.push(200);
      } else {
        // 없으면
        codes.push(404);
      }
    } else if (command === "WITHDRAW") {
      if (accountIdx !== -1) {
        const withDrawedAmount = accounts[accountIdx].amount - parseInt(number);
        // 최대한도 초과?
        if (accounts[accountIdx].limit > withDrawedAmount) {
          // 출금 안하고 403
          codes.push(403);
        } else {
          // 출금처리후
          accounts[accountIdx].amount = withDrawedAmount;
          // 200
          codes.push(200)
        }
      } else {
        // 없으면 404
        codes.push(404);
      }
    }
  }
  return codes;
}

solution(["DEPOSIT 3a 10000", "CREATE 3a 300000" , "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]);