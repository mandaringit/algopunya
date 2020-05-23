-- 코드를 입력하세요
SELECT GAME_USERS.ID,COUNT(PURCHASES.ID) AS PURCHASE_COUNT ,IFNULL(SUM(CHARACTERS.PRICE),0) AS TOTAL_PRICE FROM GAME_USERS
LEFT JOIN PURCHASES ON GAME_USERS.ID = PURCHASES.USER_ID
LEFT JOIN CHARACTERS ON PURCHASES.ITEM = CHARACTERS.NAME
GROUP BY GAME_USERS.ID