# # -- 코드를 작성해주세요


SELECT EMP_NO, EMP_NAME, 
    (CASE
        WHEN SCORE >=96 THEN 'S'
        WHEN SCORE >=90 THEN 'A'
        WHEN SCORE >=80 THEN 'B'
        ELSE 'C'
     END
    ) AS GRADE,
    
    (CASE
        WHEN SCORE >=96 THEN SAL * 0.2
        WHEN SCORE >=90 THEN SAL * 0.15
        WHEN SCORE >=80 THEN SAL *0.1
        ELSE SAL * 0
     END
    ) AS BONUS
FROM (   
    SELECT E.EMP_NO, E.EMP_NAME, SAL, SCORE
    FROM HR_EMPLOYEES E JOIN (
        SELECT EMP_NO, AVG(SCORE) AS SCORE
        FROM HR_GRADE
        GROUP BY EMP_NO) AS G ON E.EMP_NO = G.EMP_NO
    ) AS T