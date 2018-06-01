daCount = 5

incdr_header = ['dwhIdentifier', 'chargePartyDistributed', 'chargePartySingle', 'chargingUnitsAddition', 'trafficCase', 'serviceClass', 'accountValueBeforeCall', 'accountValueAfterCall', 'dedicatedAccountID1', 'dedicatedAccountValuesBeforeCall1', 'dedicatedAccountValuesAfterCall1', 'dedicatedAccountID2', 'dedicatedAccountValuesBeforeCall2', 'dedicatedAccountValuesAfterCall2', 'dedicatedAccountID3', 'dedicatedAccountValuesBeforeCall3', 'dedicatedAccountValuesAfterCall3', 'dedicatedAccountID4', 'dedicatedAccountValuesBeforeCall4', 'dedicatedAccountValuesAfterCall4', 'dedicatedAccountID5', 'dedicatedAccountValuesBeforeCall5', 'dedicatedAccountValuesAfterCall5', 'finalChargeofCall', 'chargedDuration', 'cDRType', 'teleserviceCode', 'subscriberNumber', 'date', 'time', 'faFIndicator', 'numberOfSDPInterrogations', 'subscriptionType', 'regionChargingOrigin', 'triggerTime', 'originatingLocationInformation', 'callingPartyNumber', 'calledPartyNumber', 'redirectingNumber', 'accountNumber', 'terminatingLocationInformation', 'calledPartyNumber2', 'calledPartyNumber3', 'deviceID', 'gSMCallReferenceNumber', 'serviceOfferings', 'accountGroup', 'filenameSequence', 'accumulatorID1', 'accumulatorID2', 'accumulatorID3', 'accumulatorID4', 'accumulatorID5', 'accumulatorValue1  ', 'accumulatorValue2  ', 'accumulatorValue3  ', 'accumulatorValue4  ', 'accumulatorValue5  ', 'presentationIndicator']
postcdr_header = ['Network Call Reference', 'A', 'B', 'date', 'time', 'Duration', 'Total Charged']
beepcdr_header = ['id', 'A', 'B', 'dateTime']

is_service_class_valid = "select count(1) from cmb_serviceclass where id in ('{serviceClass}')"

RevenueCalculatorQuery = "SELECT pic.id AS 'id', pic.serviceClass_id, " \
                         "pic.accountValueBeforeCall, pic.accountValueAfterCall, " \
    "pic.callCharge, " \
    "pic.callerNumber, " \
    "pic.calledNumber, " \
    "pic.callStartTime AS 'pic_starttime', " \
    "bc.callStartTime AS 'bc_starttime', " \
    "dim.DedicatedAccount, " \
    "dim.valueBeforeCall, " \
    "dim.valueAfterCall, " \
    "(callCharge * inMobilesPercentage / 100) revenue  " \
    "FROM " \
    "cmb_incdr pic, " \
    "cmb_daincdrmap dim, " \
    "cmb_serviceclass sc, " \
    "cmb_dedicatedaccount da, " \
    "cmb_beepcdr bc  " \
    "WHERE " \
    "pic.id = dim.InCdr_id " \
    "AND da.id = dim.DedicatedAccount " \
    "AND sc.id = pic.serviceClass_id " \
    "AND (pic.calledNumber = bc.callerNumber " \
    "AND pic.callerNumber = bc.calledNumber) " \
    "AND pic.callStartTime IN (SELECT " \
    "MAX(pic.callStartTime) " \
    "FROM " \
    "cmb_daincdrmap in_dim " \
    "WHERE " \
    "in_dim.DedicatedAccount = dim.DedicatedAccount) " \
    "AND ((pic.callerNumber NOT IN (SELECT " \
    "msisdn " \
    "FROM " \
    "cmb_exceptionlist " \
    "WHERE " \
    "msisdnType_id = 1) " \
    "AND (pic.calledNumber NOT IN (SELECT " \
    "msisdn " \
    "FROM " \
    "cmb_exceptionlist " \
    "WHERE " \
    "msisdnType_id = 2))) " \
    "OR ((SELECT " \
    "pic.callerNumber " \
    "FROM " \
    "cmb_exceptionlist " \
    "WHERE " \
    "msisdnType_id = 3) " \
    "AND (SELECT " \
    "pic.calledNumber " \
    "FROM " \
    "cmb_exceptionlist " \
    "WHERE " \
    "msisdnType_id = 3))) " \
    "AND TIMESTAMPDIFF(MINUTE, " \
    "bc.callStartTime, " \
    "pic.callStartTime) <= %s " \
    "AND DATEDIFF(SYSDATE(), bc.createdDate) <= %s " \
    "AND pic.subscriberType = 1 "

# Revenue calculator for PostPaid CDR

postpaidRevenueQuery = "SELECT " \
    "a.id AS 'id', " \
    "a.callCharge, " \
    "a.callerNumber, " \
    "a.calledNumber, " \
    "a.callStartTime AS 'pic_starttime', " \
    "(callCharge * inMobilesPercentage / 100) revenue " \
    "from cmb_incdr a, cmb_beepcdr b, cmb_serviceclass c " \
    "where (a.calledNumber = b.callerNumber and a.callerNumber = b.calledNumber) " \
    "and a.serviceClass_id = c.id " \
    "and TIMESTAMPDIFF(MINUTE, " \
    "b.callStartTime, " \
    "a.callStartTime) <= %s " \
    "AND DATEDIFF(SYSDATE(), b.createdDate) <= %s " \
    "and a.subscriberType = 2 "


# Queries for reporting functianality

# Report 1
report1 = """
select distinct sc.id as 'Servie Class ID', sc.description as 'Service Name', 'InMobiles' as 'Partner Name', pic.calledNumber as 'Called Party', pic.callerNumber as 'Calling Party',
pic.chargedDuration as 'Call Duration', pic.callStartTime as 'Call Time', pic.callCharge as 'Total Charge',
sc.inMobilesPercentage as 'Partner Revenue Share percentage', pic.revenueShared as 'Partner Share',
sc.otherOperatorPercentage as 'MIC1 Revenue Share percentage', da.product as 'Dedicated Account', bc.callStartTime as 'Beep Time'
from cmb_serviceclass sc
inner join cmb_incdr pic on pic.serviceClass_id = sc.id
inner join cmb_daincdrmap dam on pic.id = dam.InCdr_id
inner join cmb_dedicatedaccount da on dam.dedicatedAccount = da.id
left join cmb_beepcdr bc on (pic.callerNumber=bc.calledNumber and pic.calledNumber=bc.callerNumber)
where pic.callStartTime between str_to_date('%s','%%Y-%%m-%%d') and str_to_date('%s','%%Y-%%m-%%d')
"""





# Report 2 - Revenue Report

revenueReport = """select sum(chargedDuration) as 'Total Calls Duration', sum(callCharge) as 'Total Charge', sum(revenueShared) as 'Partner Revenue',sum(MICRevenue) as 'MIC1 Revenue', sum(revenueShared) * 2 as 'Total Revenue', date_format(pic.callStartTime, '%s') as 'Time', da.product as 'Dedicated Account' from cmb_incdr pic, cmb_daincdrmap di, cmb_dedicatedaccount da where pic.id = di.InCdr_id and di.dedicatedAccount = da.id and callStartTime between str_to_date('%s','%%Y-%%m-%%d %%H') and str_to_date('%s','%%Y-%%m-%%d %%H') and revenueShared is not null and revenueShared <> '' group by date_format(pic.callStartTime, '%s'), da.product  order by 5 """


# Report 3 - Non Revenue Report

nonRevenueReport = """
select distinct sc.description as 'Service Class', 'InMobiles' as 'Partner Name',
pic.calledNumber as 'Called Party', pic.callerNumber as 'Calling Party',
pic.chargedDuration as 'Call Duration', pic.callStartTime as 'Call Time',
pic.NCR as 'NCR', pic.reason as 'Failure Reason', bc.MCID as 'MCID', da.product as 'Dedicated Account'
FROM
    cmb_incdr pic,
    cmb_daincdrmap dim,
    cmb_serviceclass sc,
    cmb_dedicatedaccount da,
    cmb_beepcdr bc
WHERE
    pic.id = dim.InCdr_id
        AND da.id = dim.DedicatedAccount
        AND sc.id = pic.serviceClass_id
        AND (pic.calledNumber = bc.callerNumber
        AND pic.callerNumber = bc.calledNumber)
and pic.callStartTime between str_to_date('%s','%%Y-%%m-%%d') and str_to_date('%s','%%Y-%%m-%%d')
and pic.reason is not null
"""

# Statistics 1 - 1

beep_info = """
select count(*) as 'Total Beeps',
count(distinct callerNumber) as 'Unique Calling Parties',
count(distinct calledNumber) as 'Unique Called Parties'
from cmb_beepcdr a
where callStartTime between str_to_date('%s','%%Y-%%m-%%d') and str_to_date('%s','%%Y-%%m-%%d')
"""

cdrinfo = """
select count(*) as 'Count of Callbacks', avg(b.chargedDuration) as 'Average Duration per call back', sum(b.chargedDuration) as 'Total Call Duration'
 from cmb_beepcdr a, cmb_incdr b where a.calledNumber = b.callerNumber and a.callerNumber=b.calledNumber
and a.callStartTime between str_to_date('%s','%%Y-%%m-%%d') and str_to_date('%s','%%Y-%%m-%%d')
"""


updateReasonMoreThan1HourPrepaid = """
update cmb_incdr 
set reason = 'Late call back'
where (revenueShared is null or revenueShared = '') and (reason is null or reason = '')
and subscriberType=1;
"""

updateReasonMoreThan1HourPostpaid = """
update cmb_incdr 
set reason = 'Late call back'
where (revenueShared is null or revenueShared = '') and (reason is null or reason = '')
and subscriberType=2;
"""