# -- 코드를 입력하세요
# SELECT APNT_NO,	PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME,	A.APNT_YMD
# FROM DOCTOR D JOIN APPOINTMENT A ON D.DR_ID = A.MDDR_ID  JOIN PATIENT P ON P.PT_NO = A.PT_NO
# WHERE YEAR(APNT_YMD) ='2022' AND MONTH(APNT_YMD) = '04' AND DAY(APNT_YMD) = '13'
#     AND APNT_CNCL_YN ='N' AND A.MCDP_CD = 'CS'

SELECT APNT_NO,	PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME,	A.APNT_YMD
FROM DOCTOR D JOIN APPOINTMENT A ON D.DR_ID = A.MDDR_ID  JOIN PATIENT P ON P.PT_NO = A.PT_NO
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m-%d') ='2022-04-13'
    AND APNT_CNCL_YN ='N' AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD ASC;

# SELECT DATE_FORMAT(APNT_YMD, '%Y-%m-%d')
# FROM DOCTOR D JOIN APPOINTMENT A ON D.DR_ID = A.MDDR_ID  JOIN PATIENT P ON P.PT_NO = A.PT_NO

