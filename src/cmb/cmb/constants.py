is_service_class_valid = "select count(1) from cmb_serviceclass where id in ('{serviceClass}')"

RevenueCalculatorQuery = """
SELECT
    pic.id AS 'CDRID',
    pic.serviceClass_id,
    pic.accountValueBeforeCall,
    pic.accountValueAfterCall,
    pic.callCharge,
    pic.callerNumber,
    pic.calledNumber,
    pic.callStartTime AS 'pic_starttime',
    bc.callStartTime AS 'bc_starttime',
    dim.DedicatedAccount,
    dim.valueBeforeCall,
    dim.valueAfterCall,
    (callCharge * inMobilesPercentage / 100) revenue
FROM
    cmb_prepaidincdr pic,
    cmb_daincdrmap dim,
    cmb_serviceclass sc,
    cmb_dedicatedaccount da,
    cmb_beepcdr bc
WHERE
    pic.id = dim.PrepaidInCdr_id
        AND da.id = dim.DedicatedAccount_id
        AND sc.id = pic.serviceClass_id
        AND (pic.calledNumber = bc.calledNumber
        AND pic.callerNumber = bc.callerNumber)
        AND pic.callStartTime IN (SELECT
            MAX(pic.callStartTime)
        FROM
            cmb_daincdrmap in_dim
        WHERE
            in_dim.DedicatedAccount_id = dim.DedicatedAccount_id)
        AND ((pic.callerNumber NOT IN (SELECT
            msisdn
        FROM
            cmb_exceptionlist
        WHERE
            msisdnType_id = 1)
        AND (pic.calledNumber NOT IN (SELECT
            msisdn
        FROM
            cmb_exceptionlist
        WHERE
            msisdnType_id = 2)))
        OR ((SELECT
            pic.callerNumber
        FROM
            cmb_exceptionlist
        WHERE
            msisdnType_id = 3)
        AND (SELECT
            pic.calledNumber
        FROM
            cmb_exceptionlist
        WHERE
            msisdnType_id = 3)))
        AND TIMESTAMPDIFF(MINUTE,
        bc.callStartTime,
        pic.callStartTime) <= %s
        AND DATEDIFF(SYSDATE(), bc.createdDate) <= %s
        """
