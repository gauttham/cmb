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
    pic.callStartTime as 'pic starttime',
    bc.callStartTime  as 'bc starttime',
    dim.DedicatedAccount_id,
    dim.valueBeforeCall,
    dim.valueAfterCall,
    callCharge * inMobilesPercentage/100 revenue
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
        AND

        TIMESTAMPDIFF(MINUTE,
        bc.callStartTime,
        pic.callStartTime) <= {BeepToCallGap}
        and datediff(sysdate(), bc.createdDate) <={timeDuration}
"""
